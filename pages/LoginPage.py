from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "login-username"
    password_field_id = "login-password"
    login_button_id = "login-button"

    error_message_invalid_credentials = "//span[contains(text(),'Incorrect username or password.')]"

    def enter_email_username_element(self,email_address_text):
        self.type_element(email_address_text,"email_address_field_id",self.email_address_field_id)


    def enter_password_element(self, password_text):
        self.type_element(password_text,"password_field_id", self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_id", self.login_button_id)
        return AccountPage(self.driver)

    def login_with_credentials(self,email_address_text, password_text):
        self.enter_email_username_element(email_address_text)
        self.enter_password_element(password_text)
        return self.click_on_login_button()


    def display_message_invalid_credentials(self):
        self.retrieve_element_text("error_message_invalid_credentials", self.error_message_invalid_credentials)
