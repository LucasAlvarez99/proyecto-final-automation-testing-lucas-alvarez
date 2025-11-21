from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_completo(browser):
    login = LoginPage(browser)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    inventario = InventoryPage(browser)
    inventario.agregar_producto_backpack()
    inventario.ir_al_carrito()

    carrito = CartPage(browser)
    carrito.ir_a_checkout()

    paso1 = CheckoutStepOnePage(browser)
    paso1.completar_formulario("Lucas", "Alvarez", "1234")
    paso1.continuar()

    paso2 = CheckoutStepTwoPage(browser)
    paso2.finalizar()

    final = CheckoutCompletePage(browser)

    assert final.obtener_mensaje_final() == "Checkout: Complete!"
