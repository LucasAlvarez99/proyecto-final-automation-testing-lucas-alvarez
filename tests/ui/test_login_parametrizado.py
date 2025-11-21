import pytest
from utils.data_reader import load_csv_data
from pages.login_page import LoginPage

# Cargar CSV completo
users = load_csv_data("user.csv")

@pytest.mark.parametrize("user", users)
def test_login_parametrizado(browser, user):
    login_page = LoginPage(browser)
    login_page.open()

    username = user["username"]
    password = user["password"]

    login_page.login(username, password)

    if username == "standard_user" and password == "secret_sauce":
        assert login_page.is_login_successful()
    else:
        assert login_page.is_error_message_displayed()
