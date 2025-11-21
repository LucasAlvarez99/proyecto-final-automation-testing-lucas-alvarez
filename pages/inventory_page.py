from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def obtener_titulo(self):
        return self.obtener_texto(self.TITLE)

    def agregar_producto_backpack(self):
        self.click(self.ADD_BACKPACK)

    def ir_al_carrito(self):
        self.click(self.CART_BUTTON)
