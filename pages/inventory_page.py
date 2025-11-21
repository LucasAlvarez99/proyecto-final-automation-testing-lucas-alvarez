from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CSS_SELECTOR, ".title")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_ICON = (By.ID, "shopping_cart_container")

    def is_page_loaded(self):
        return self.is_visible(self.TITLE)

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)
