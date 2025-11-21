"""
Cart Page - Página del carrito de compras de SauceDemo.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object para la página del carrito."""

    # Localizadores
    TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")

    def obtener_titulo(self):
        """Obtiene el título de la página del carrito."""
        # Esperar a que el título sea visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return self.obtener_texto(self.TITLE)

    def ir_a_checkout(self):
        """
        Hace clic en el botón Checkout.
        Usa JavaScript click como fallback.
        """
        try:
            checkout_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
            )
            checkout_btn.click()
        except Exception:
            # Fallback con JavaScript
            checkout_btn = self.driver.find_element(*self.CHECKOUT_BUTTON)
            self.driver.execute_script("arguments[0].click();", checkout_btn)
        
        # Esperar a que navegue al checkout
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )

    def contar_items(self):
        """Cuenta cuántos items hay en el carrito."""
        items = self.driver.find_elements(*self.CART_ITEM)
        return len(items)

    def continuar_comprando(self):
        """Vuelve a la página de inventario."""
        self.click(self.CONTINUE_SHOPPING)