import allure
from pages.Homepage import HomePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_for_an_existing_song(self):
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        search_page = home_page.enter_song_into_search_box_field("Disturbed")
        assert search_page.display_status_of_song()

    @allure.severity(allure.severity_level.MINOR)
    def test_search_for_an_empty_song(self):
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        home_page.enter_empty_value_into_search_box_field()
        expected_text = "Please make sure your words are spelled correctly, or use fewer or different keywords."
        search_page = SearchPage(self.driver)
        assert search_page.display_error_message_no_result_found().__eq__(expected_text)
