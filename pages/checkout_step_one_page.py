"""
Checkout Step One Page - Formulario de datos de envío.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Page Object para el paso 1 del checkout (datos de envío)."""

    # Localizadores
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def completar_formulario(self, nombre, apellido, codigo_postal):
        """
        Completa el formulario de datos de envío.
        
        Args:
            nombre: Primer nombre
            apellido: Apellido
            codigo_postal: Código postal
        """
        self.escribir(self.FIRST_NAME, nombre)
        self.escribir(self.LAST_NAME, apellido)
        self.escribir(self.POSTAL_CODE, codigo_postal)

    def continuar(self):
        """Hace clic en el botón Continue para ir al paso 2."""
        try:
            continue_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONTINUE_BUTTON)
            )
            continue_btn.click()
        except Exception:
            continue_btn = self.driver.find_element(*self.CONTINUE_BUTTON)
            self.driver.execute_script("arguments[0].click();", continue_btn)

    def cancelar(self):
        """Cancela el checkout y vuelve al carrito."""
        self.click(self.CANCEL_BUTTON)

    def obtener_error(self):
        """Obtiene el mensaje de error si existe."""
        try:
            error = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error.text
        except:
            return None