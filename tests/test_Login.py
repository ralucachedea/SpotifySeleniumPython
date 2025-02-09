from datetime import datetime
import allure
import pytest
from pages.Homepage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtilities


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("log_on_failure")
class TestLogin(BaseTest):
    @pytest.mark.parametrize("username, password", ExcelUtilities.get_data_from_excel("ExcelFiles/credentials.xlsx","TestLogin"))
    def test_login_with_valid_credentials(self, username, password):
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_login_link()
        account_page = login_page.login_with_credentials(username,password)
        assert account_page.display_status_of_account_information_user()

    def test_login_with_valid_email_invalid_password(self):
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_login_link()
        login_page.login_with_credentials("raluca@chedea.eu","test")
        expected_error_message = "Incorrect username or password."
        assert login_page.error_message_invalid_credentials.__contains__(expected_error_message)

    def test_login_with_invalid_email_valid_password(self):
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        home_page.click_on_login_link()
        login_page = LoginPage(self.driver)
        login_page.login_with_credentials(self.generate_email_with_time_stamp(),"ParolaSpotify001")
        login_page.enter_email_username_element(self.generate_email_with_time_stamp())
        login_page.enter_password_element("ParolaSpotify001")
        login_page.click_on_login_button()
        expected_error_message = "Incorrect username or password."
        assert login_page.error_message_invalid_credentials.__contains__(expected_error_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d")
        return "raluca" + time_stamp + "@gmail.com"