import pytest
from pages.login_page import LoginPage
from utils.data_reader import read_json

def test_login_valido(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    # Validar redirección a inventory y título
    from pages.inventory_page import InventoryPage
    inv = InventoryPage(driver)
    assert "Products" in inv.titulo()
    assert "inventory" in driver.current_url

@pytest.mark.parametrize("cred", read_json("datos/usuarios.json"))
def test_login_parametrizado(driver, cred, request):
    request.node.nombre_captura = f"login_{cred['username']}"
    login = LoginPage(driver)
    login.load()
    login.login(cred["username"], cred["password"])
    # Si es locked_out_user, debe mostrar error
    if cred["username"] == "locked_out_user":
        assert "locked out" in login.get_error().lower()
    else:
        from pages.inventory_page import InventoryPage
        inv = InventoryPage(driver)
        assert inv.titulo() == "Products"
