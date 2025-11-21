import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def esperar_elemento_visible(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))

def esperar_elemento_presente(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))

def esperar_clickable(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))

def tomar_captura(driver, nombre_archivo):
    try:
        carpeta = "screenshots"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        path = os.path.join(carpeta, f"{timestamp}-{nombre_archivo}.png")
        resultado = driver.save_screenshot(path)
        if resultado:
            return path
        return None
    except Exception as e:
        print(f"Error al tomar captura: {e}")
        return None
