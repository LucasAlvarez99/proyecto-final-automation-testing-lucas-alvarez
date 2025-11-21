from selenium.webdriver.common.by import By
from utils.helpers import esperar_elemento_visible, esperar_clickable

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def remover_primer_producto(self):
        btns = self.driver.find_elements(By.CLASS_NAME, "cart_button")
        if btns:
            btns[0].click()

    def contador_carrito(self):
        try:
            el = esperar_elemento_visible(self.driver, By.CLASS_NAME, "shopping_cart_badge", timeout=5)
            return int(el.text)
        except:
            return 0
