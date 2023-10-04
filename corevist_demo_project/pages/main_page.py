import time

import allure
from selene import browser, have, be, command


class MainPage:
    def __init__(self):
        self.mid_page_section = browser.element('.fusion-title-heading p')
        self.scroll_to_top_button = browser.element('a#toTop')
        self.title = browser.element('.post-content h1')

    @allure.step('Scroll to the mid page section')
    def scroll_to_mid_page_section(self):
        self.mid_page_section.perform(command.js.scroll_into_view)
        time.sleep(2)
        return self

    @allure.step('Click on Scroll to Top button')
    def click_on_scroll_to_top_button(self):
        self.scroll_to_top_button.perform(command.js.click)
        time.sleep(2)

    @allure.step('Main Page should have title {title}')
    def should_have_correct_title(self, title):
        self.title.should(be.visible)
        self.title.should(have.exact_text(title))
