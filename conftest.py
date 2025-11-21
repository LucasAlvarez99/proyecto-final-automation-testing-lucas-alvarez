import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import tomar_captura, ensure_dir

# Carpeta para screenshots y reports
ensure_dir("screenshots")
ensure_dir("reports")

def _create_chrome_options(headless=False):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if headless:
        options.add_argument("--headless=new")
    return options

@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture que crea el WebDriver.
    - Por defecto usa webdriver-manager (auto descarga).
    - Si querés usar un chromedriver local, setear la variable de entorno CHROME_DRIVER_PATH.
    """
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    chrome_path = os.getenv("CHROME_DRIVER_PATH", "")

    options = _create_chrome_options(headless=headless)

    if chrome_path:
        service = Service(chrome_path)
    else:
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    request.node._driver = driver
    yield driver

    # Nombre de captura (si fue seteado por el test)
    nombre_captura = getattr(request.node, "nombre_captura", None)
    if not nombre_captura:
        nombre_captura = f"{request.node.name}_finalizado"
    path = tomar_captura(driver, nombre_captura)
    print(f"Screenshot guardado: {path}")

    driver.quit()
