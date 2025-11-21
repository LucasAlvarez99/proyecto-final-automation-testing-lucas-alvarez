from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    TITLE = (By.CLASS_NAME, "title")

    def obtener_mensaje_final(self):
        return self.obtener_texto(self.TITLE)
