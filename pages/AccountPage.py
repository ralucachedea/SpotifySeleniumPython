from pages.BasePage import BasePage

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # account_page_user_logo_xpath = "//button[contains(@class,'Button-sc-1dqy6lx-0 eA-Dwob encore-text-body-medium-bold e-9541-overflow-wrap-anywhere KAq2kDjXj2VS4eXrFL4i')]"
    account_page_user_logo_css = "span[data-testid = 'username-first-letter']"

    def display_status_of_account_information_user(self):
        return self.retrieve_element_text("account_page_user_logo_css",self.account_page_user_logo_css)
