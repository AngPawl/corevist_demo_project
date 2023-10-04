import allure
from selene import browser, have


class LiveChat:
    def __init__(self):
        self.welcome_message_box = browser.element('#welcome-message')
        self.chat_box_header = browser.element('[data-test-id="widget-header-name"]')

    @allure.step('Open live chat box')
    def open_chat_box(self):
        self.welcome_message_box.click()

    @allure.step('Opened live chat box header should contain company name {name}')
    def opened_chat_box_header_should_contain_company_name(self, name):
        self.chat_box_header.should(have.exact_text(name))
