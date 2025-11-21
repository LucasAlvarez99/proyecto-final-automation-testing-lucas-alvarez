import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
from utils.logger import get_logger


@pytest.fixture
def browser(request):
    """
    Fixture que inicializa el navegador Chrome para las pruebas de UI.
    Captura screenshot automaticamente si la prueba falla.
    """
    logger = get_logger(request.node.name)
    logger.info("=== Iniciando prueba: %s ===" % request.node.name)
    logger.info("Configurando navegador Chrome...")

    # Configuracion de Chrome con opciones de estabilidad
    chrome_options = Options()
    
    # Opciones para mayor estabilidad en Windows
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Evitar deteccion de automatizacion
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # Preferencias adicionales
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Descomentar para modo headless:
    # chrome_options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Configurar timeouts
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    
    logger.info("Navegador iniciado correctamente")

    yield driver

    # Captura de screenshot si la prueba fallo
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        logger.error("[FAILED] La prueba FALLO - Generando captura de pantalla...")
        _capture_screenshot(driver, request, logger)
    else:
        logger.info("[PASSED] Prueba completada")

    logger.info("Cerrando navegador...")
    try:
        driver.quit()
    except Exception as e:
        logger.warning(f"Error al cerrar navegador: {e}")
    logger.info("=== Fin de prueba: %s ===" % request.node.name)


def _capture_screenshot(driver, request, logger):
    """Funcion auxiliar para capturar screenshots en caso de fallo."""
    # Verificar si la sesion del navegador sigue activa
    try:
        _ = driver.current_url
    except Exception:
        logger.warning("Navegador cerrado - no se puede capturar screenshot")
        return
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    screenshot_dir = os.path.join(base_path, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"{request.node.name}_{timestamp}.png"
    file_path = os.path.join(screenshot_dir, file_name)

    try:
        driver.save_screenshot(file_path)
        logger.info(f"Screenshot guardado en: {file_path}")
    except Exception as e:
        logger.error(f"Error al guardar screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que permite acceder al resultado de la prueba
    desde el fixture 'browser' para capturar screenshots en fallos.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session", autouse=True)
def configure_reports():
    """
    Fixture de sesion para configurar directorios de reportes.
    Se ejecuta una vez al inicio de toda la sesion de pruebas.
    """
    directories = ["screenshots", "logs", "reports"]
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
    
    yield