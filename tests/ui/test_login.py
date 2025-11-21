import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_page_loaded(), "❌ No se cargó la Inventory Page"

def test_login_fallido(driver):
    login = LoginPage(driver)

    login.open()
    login.login("usuario_incorrecto", "clave_incorrecta")

    error = login.get_error_message()
    assert "Epic sadface" in error, "❌ El mensaje de error no apareció"
