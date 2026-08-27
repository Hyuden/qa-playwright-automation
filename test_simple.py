from playwright.sync_api import Page, expect

def test_login_exitoso(page: Page):
    # 1. Navegar a la página web
    page.goto("https://the-internet.herokuapp.com/login")

    # 2. Localizar elementos e interactuar (Playwright espera los elementos automáticamente)
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    
    # 3. Hacer clic en el botón de submit
    page.get_by_role("button", name="Login").click()

    # 4. Aserción web inteligente (espera a que el elemento sea visible y contenga el texto)
    mensaje_flash = page.locator("#flash")
    expect(mensaje_flash).to_be_visible()
    expect(mensaje_flash).to_contain_text("You logged into a secure area!")