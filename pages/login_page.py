from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def abrir(self):
        self.navegar("https://www.saucedemo.com/")

    def login(self, username, password):
        self.escribir(self.USERNAME_INPUT, username)
        self.escribir(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def obtener_mensaje_error(self):
        return self.obtener_texto(self.ERROR_MSG)
