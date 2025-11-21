from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def completar_formulario(self, nombre, apellido, codigo):
        self.escribir(self.FIRST_NAME, nombre)
        self.escribir(self.LAST_NAME, apellido)
        self.escribir(self.POSTAL_CODE, codigo)

    def continuar(self):
        self.click(self.CONTINUE_BUTTON)
