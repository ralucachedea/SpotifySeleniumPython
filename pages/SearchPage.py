from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_song_link_text = "Songs"
    error_message_no_result_found_css = ".W37c8X5LCtHtmryEzR4I"

    def display_status_of_song(self):
        return self.check_display_status_of_element("valid_song_link_text", self.valid_song_link_text)

    def display_error_message_no_result_found(self):
        return self.retrieve_element_text("error_message_no_result_found_css", self.error_message_no_result_found_css)
