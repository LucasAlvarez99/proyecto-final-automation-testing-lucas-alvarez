from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_producto_al_carrito(browser):
    login = LoginPage(browser)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    inventario = InventoryPage(browser)
    inventario.agregar_producto_backpack()
    inventario.ir_al_carrito()

    carrito = CartPage(browser)

    assert carrito.obtener_titulo() == "Your Cart"
