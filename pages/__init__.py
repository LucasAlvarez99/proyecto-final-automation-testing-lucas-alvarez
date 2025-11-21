"""
Page Object Model - Módulo de páginas
=====================================

Este módulo contiene las clases que representan cada página de la aplicación
SauceDemo, siguiendo el patrón Page Object Model (POM).

Páginas disponibles:
- BasePage: Clase base con métodos comunes
- LoginPage: Página de inicio de sesión
- InventoryPage: Página de productos/inventario
- CartPage: Página del carrito de compras
- CheckoutStepOnePage: Formulario de datos de envío
- CheckoutStepTwoPage: Resumen de la compra
- CheckoutCompletePage: Confirmación de compra exitosa
"""

from .base_page import BasePage
from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage
from .checkout_step_one_page import CheckoutStepOnePage
from .checkout_step_two_page import CheckoutStepTwoPage
from .checkout_complete_page import CheckoutCompletePage

__all__ = [
    'BasePage',
    'LoginPage',
    'InventoryPage',
    'CartPage',
    'CheckoutStepOnePage',
    'CheckoutStepTwoPage',
    'CheckoutCompletePage'
]