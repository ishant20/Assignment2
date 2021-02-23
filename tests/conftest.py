import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/ishant/PycharmProjects/zestAssignment/Utilities/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/ishant/PycharmProjects/zestAssignment/Utilities/geckodriver")
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()




