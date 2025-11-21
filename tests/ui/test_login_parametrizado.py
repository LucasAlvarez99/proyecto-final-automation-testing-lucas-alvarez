import pytest
from pages.login_page import LoginPage
from utils.data_reader import leer_csv

datos = leer_csv("user.csv")

@pytest.mark.parametrize("fila", datos)
def test_login_parametrizado(browser, fila):

    login = LoginPage(browser)
    login.abrir()

    login.login(fila["username"], fila["password"])

    if fila["resultado"] == "ok":
        # login exitoso → inventario
        assert "inventory" in browser.current_url
    else:
        # login fallido
        assert "Epic sadface" in login.obtener_mensaje_error()
