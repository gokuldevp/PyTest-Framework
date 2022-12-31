import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service(r"D:\Development\driver\Chrome\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service(r"D:\Development\driver\Edge\msedgedriver.exe")
        driver =  webdriver.Edge(service=serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service(r"D:\Development\driver\Firefox\geckodriver.exe")
        driver =  webdriver.Firefox(service=serv_obj)
    driver.maximize_window()
    return driver


def pytest_addoption(parser):  # This will get the value from Command line
    parser.addoption("--browser")

@pytest.fixture()  # This will return the browser value to the setup method
def browser(request):
    return request.config.getoption("--browser")

# Customize HTML reports
# Hook for adding Evironment info to HTML report
def pytest_configure(config):
    config._metadata["Project Name"] = "Orange HRM"
    config._metadata["Module Name"] = "Login Module"
    config._metadata["Tester Name"] = "Gokul Dev P"
    config._metadata["OS Name"] = "Windows 11"

# Hook for Deleting/Modify Evironment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Packages",None)
    metadata.pop("Platform", None)
    metadata.pop("Plugins", None)
