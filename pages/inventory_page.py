"""
Inventory Page - Página de productos/inventario de SauceDemo.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object para la página de inventario/productos."""

    # Localizadores
    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")

    def obtener_titulo(self):
        """Obtiene el título de la página."""
        return self.obtener_texto(self.TITLE)

    def agregar_producto_backpack(self):
        """Agrega el producto 'Sauce Labs Backpack' al carrito."""
        self.click(self.ADD_BACKPACK)
        # Esperar a que aparezca el badge del carrito (indica que se agregó)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
        except:
            pass  # El badge puede no aparecer si ya había items

    def ir_al_carrito(self):
        """
        Navega al carrito de compras.
        Usa JavaScript click como fallback si el click normal falla.
        """
        try:
            # Esperar a que el enlace del carrito sea clickeable
            cart_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CART_LINK)
            )
            cart_element.click()
        except Exception:
            # Fallback: usar JavaScript para hacer click
            cart_element = self.driver.find_element(*self.CART_LINK)
            self.driver.execute_script("arguments[0].click();", cart_element)
        
        # Esperar a que la URL cambie a cart.html
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart.html")
        )

    def contar_productos(self):
        """Cuenta cuántos productos hay en la página."""
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        return len(items)

    def obtener_cantidad_carrito(self):
        """Obtiene el número mostrado en el badge del carrito."""
        try:
            badge = self.encontrar(self.CART_BADGE, timeout=3)
            return int(badge.text)
        except:
            return 0