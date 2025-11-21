import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or safari"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "safari":
        driver = webdriver.Safari()
        driver.set_window_size(1280, 720)
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    else:  # CHROME за замовчуванням
        options = Options()
        # options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,720")
        options.add_argument("--disable-features=PasswordLeakDetection")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
