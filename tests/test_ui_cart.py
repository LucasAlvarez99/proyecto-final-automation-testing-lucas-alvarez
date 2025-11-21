import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_y_verificar_carrito(driver, request):
    request.node.nombre_captura = "ui_agregar_carrito"
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(driver)
    inv.agregar_primer_producto()

    # verificar contador
    cart = CartPage(driver)
    assert cart.contador_carrito() == 1

    # ir al carrito y validar item
    inv.ir_al_carrito()
    items = cart.items()
    assert len(items) >= 1
