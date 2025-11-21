from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_producto_al_carrito(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    assert cart.is_page_loaded(), "❌ No se cargó el carrito correctamente"
