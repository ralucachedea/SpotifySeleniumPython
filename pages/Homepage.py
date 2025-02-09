from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name_css = "input[placeholder='What do you want to play?']"
    login_link_xpath = "//span[contains(text(),'Log in')]"


    def enter_song_into_search_box_field(self, song_name):
        self.driver.find_element(By.CSS_SELECTOR, self.search_box_field_name_css).send_keys(song_name)
        self.driver.find_element(By.CSS_SELECTOR, self.search_box_field_name_css).send_keys(Keys.ENTER)
        return SearchPage(self.driver)

    def enter_empty_value_into_search_box_field(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_box_field_name_css).send_keys(Keys.SPACE)

    def click_on_login_link(self):
        self.element_click("login_link_xpath",self.login_link_xpath)
        return LoginPage(self.driver)

    def retrieve_homepage_title(self):
        return self.driver.title