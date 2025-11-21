import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import pytest_html
from utils.logger import get_logger


@pytest.fixture
def browser(request):
    """Fixture que crea el navegador y captura screenshot si ocurre un fallo."""

    logger = get_logger(request.node.name)
    logger.info("Iniciando navegador Chrome")

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        logger.error("La prueba falló, generando captura...")

        base_path = os.path.dirname(os.path.abspath(__file__))
        screenshot_dir = os.path.join(base_path, "screenshot")
        os.makedirs(screenshot_dir, exist_ok=True)

        file_name = f"{request.node.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        file_path = os.path.join(screenshot_dir, file_name)

        driver.save_screenshot(file_path)
        logger.info(f"Screenshot guardado en: {file_path}")

        if hasattr(request.config, "_html"):
            extra = request.config._html.extra
            extra.append(pytest_html.extras.image(file_path))

    logger.info("Cerrando navegador")
    driver.quit()


def pytest_runtest_makereport(item, call):
    """Permite saber si una prueba falló dentro del fixture."""
    if "browser" in item.fixturenames:
        outcome = yield
        rep = outcome.get_result()

        setattr(item, "rep_" + rep.when, rep)
        return rep
