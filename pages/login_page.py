from selenium.webdriver.common.by import By
from utils.helpers import esperar_elemento_visible, esperar_clickable

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        esperar_elemento_visible(self.driver, By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        esperar_elemento_visible(self.driver, By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        esperar_clickable(self.driver, By.ID, "login-button").click()

    def get_error(self):
        el = esperar_elemento_visible(self.driver, By.XPATH, "//h3[@data-test='error']", timeout=5)
        return el.text
