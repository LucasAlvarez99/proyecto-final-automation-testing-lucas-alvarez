from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navegar(self, url):
        self.driver.get(url)

    def encontrar(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        self.encontrar(locator, timeout).click()

    def escribir(self, locator, texto, timeout=10):
        campo = self.encontrar(locator, timeout)
        campo.clear()
        campo.send_keys(texto)

    def obtener_texto(self, locator, timeout=10):
        return self.encontrar(locator, timeout).text
