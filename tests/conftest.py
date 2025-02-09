from pickle import GLOBAL
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from typing_extensions import Any
from utilities import ReadConfigurations

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

@pytest.fixture()
def setup(request):
    global driver
    browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("safari"):
        driver = webdriver.Safari()
    else:
        print("Provide a valid browser")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()