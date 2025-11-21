import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import tomar_captura
import os
import csv

@pytest.fixture(scope="session")
def load_users():
    """Carga usuarios desde CSV para parametrización."""
    users = []
    csv_path = os.path.join("data", "users.csv")
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

@pytest.fixture
def driver(request):
    """Inicializa y cierra el WebDriver automáticamente."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver

    # Si la prueba falló → tomar screenshot automáticamente
    if request.node.rep_call.failed:
        nombre_test = request.node.name
        tomar_captura(driver, nombre_test)

    driver.quit()

def pytest_runtest_makereport(item, call):
    """Hook necesario para saber si un test falló."""
    if "driver" in item.fixturenames:
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)
