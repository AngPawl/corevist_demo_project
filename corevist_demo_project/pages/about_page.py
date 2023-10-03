import allure
from selene import browser, have, be


class AboutPage:
    def __init__(self):
        self.title = browser.element('.post-content h1')

    @allure.step('About Page should have title {title}')
    def should_have_correct_title(self, title):
        self.title.should(be.visible)
        self.title.should(have.exact_text(title))
