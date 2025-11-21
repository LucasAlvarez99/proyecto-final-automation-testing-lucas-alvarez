from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_completo(driver):
    login = LoginPage(driver)
    inventario = InventoryPage(driver)
    carrito = CartPage(driver)
    paso1 = CheckoutStepOnePage(driver)
    paso2 = CheckoutStepTwoPage(driver)
    final = CheckoutCompletePage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventario.add_first_product_to_cart()
    inventario.go_to_cart()

    carrito.checkout()

    paso1.fill_form("Lucas", "Alvarez", "1000")
    paso1.continue_to_step_two()

    paso2.finish_purchase()

    assert final.is_order_complete(), "❌ No se completó la orden"
