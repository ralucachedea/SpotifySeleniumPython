from pickle import GLOBAL
import allure
from allure_commons.types import AttachmentType
from typing_extensions import Any
from webdriver_manager.core import driver
from utilities import ReadConfigurations
from selenium import webdriver

import pytest

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Any):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")

@pytest.fixture(scope="function")
def setup(request):
    driver = None

    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        print("Provide a valid browser")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield driver
    driver.quit()


