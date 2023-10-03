import time

import allure
from selene import browser, have, be
from selene.core.command import js


class MainPage:
    def __init__(self):
        self.book_a_demo_button = browser.element('a[href*="/request-a-demo"]')
        self.footer = browser.element('div.fusion-footer')
        self.scroll_to_top_button = browser.element('a#toTop')
        self.title = browser.element('.post-content h1')

    @allure.step('Open Request a Demo Page')
    def open_request_a_demo_page(self):
        self.book_a_demo_button.perform(command=js.scroll_into_view).click()

    @allure.step('Scroll to the page footer')
    def scroll_to_footer(self):
        self.footer.perform(command=js.scroll_into_view)
        time.sleep(1)
        return self

    @allure.step('Click on Scroll to Top button')
    def click_on_scroll_to_top_button(self):
        self.scroll_to_top_button.perform(command=js.click)
        time.sleep(2)

    @allure.step('Main Page should have title {title}')
    def should_have_correct_title(self, title):
        self.title.should(be.visible)
        self.title.should(have.exact_text(title))
