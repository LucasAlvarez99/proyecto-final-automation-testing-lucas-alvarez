"""
Test de Checkout Completo
=========================

Prueba end-to-end del flujo de compra en SauceDemo.
Cubre: login -> agregar producto -> carrito -> checkout -> confirmacion
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_checkout_completo(browser):
    """
    Flujo completo de compra exitosa.
    
    Pasos:
    1. Login con usuario valido
    2. Agregar producto al carrito
    3. Ir al carrito
    4. Iniciar checkout
    5. Completar datos de envio
    6. Revisar resumen
    7. Finalizar compra
    8. Verificar confirmacion
    """
    # 1. Login
    login = LoginPage(browser)
    login.abrir()
    login.login("standard_user", "secret_sauce")
    
    # Esperar a que cargue la pagina de inventario
    WebDriverWait(browser, 10).until(
        EC.url_contains("inventory.html")
    )

    # 2. Verificar que estamos en inventario y agregar producto
    inventario = InventoryPage(browser)
    titulo_inventario = inventario.obtener_titulo()
    assert titulo_inventario == "Products", \
        f"Expected 'Products', got '{titulo_inventario}'"
    
    inventario.agregar_producto_backpack()

    # 3. Ir al carrito
    inventario.ir_al_carrito()

    # 4. Verificar carrito
    carrito = CartPage(browser)
    titulo_carrito = carrito.obtener_titulo()
    assert titulo_carrito == "Your Cart", \
        f"Expected 'Your Cart', got '{titulo_carrito}'"
    
    # 5. Iniciar checkout
    carrito.ir_a_checkout()

    # 6. Completar formulario de envio
    paso1 = CheckoutStepOnePage(browser)
    paso1.completar_formulario("Lucas", "Alvarez", "1234")
    paso1.continuar()
    
    # Esperar navegacion al paso 2
    WebDriverWait(browser, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    # 7. Revisar resumen y finalizar
    paso2 = CheckoutStepTwoPage(browser)
    paso2.finalizar()

    # 8. Verificar confirmacion
    final = CheckoutCompletePage(browser)
    titulo_final = final.obtener_mensaje_final()
    
    assert titulo_final == "Checkout: Complete!", \
        f"Expected 'Checkout: Complete!' but got '{titulo_final}'"