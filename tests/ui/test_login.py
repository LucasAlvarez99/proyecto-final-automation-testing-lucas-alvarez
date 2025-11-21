from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(browser):
    login = LoginPage(browser)
    login.abrir()

    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)

    assert inventory.obtener_titulo() == "Products"
