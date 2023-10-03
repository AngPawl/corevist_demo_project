import allure
from selene import browser, have, be
from selene.support.conditions.have import exact_text


class WatchDemoModalForm:
    def __init__(self):
        self.title = browser.all('.modal-window-content h4').element_by(
            exact_text('Watch Demo')
        )
        self.close_button = browser.element(
            '[id^="wow-modal-close"].mw-close-btn[style]'
        )

    @allure.step('Close Watch Demo modal form on Close button')
    def close_by_clicking_on_close_button(self):
        self.close_button.click()

    @allure.step('Watch Demo modal form should be closed')
    def should_be_closed(self):
        self.title.should(be.not_.visible)

    @allure.step('Watch Demo modal form should have title {title}')
    def should_have_correct_title(self, title):
        self.title.should(have.exact_text(title))
