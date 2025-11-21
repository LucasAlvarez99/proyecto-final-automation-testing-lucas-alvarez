from selenium.webdriver.common.by import By
from utils.helpers import esperar_elemento_visible, esperar_clickable

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def titulo(self):
        return esperar_elemento_visible(self.driver, By.CLASS_NAME, "title", timeout=10).text

    def primer_producto(self):
        nombre = esperar_elemento_visible(self.driver, By.CLASS_NAME, "inventory_item_name", timeout=10).text
        precio = esperar_elemento_visible(self.driver, By.CLASS_NAME, "inventory_item_price", timeout=10).text
        return {"nombre": nombre, "precio": precio}

    def agregar_primer_producto(self):
        btn = esperar_clickable(self.driver, By.CLASS_NAME, "btn_inventory", timeout=10)
        btn.click()

    def ir_al_carrito(self):
        esperar_clickable(self.driver, By.CLASS_NAME, "shopping_cart_link", timeout=5).click()

    def hay_menu(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "bm-burger-button").is_displayed()
        except:
            return False
