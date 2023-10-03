import allure
from selene import browser, be, have


class BookADemoPage:
    def __init__(self):
        self.book_demo_form_title = browser.element(".post-content h4")

    @allure.step('Book Demo form title should be present on the page')
    def book_demo_form_title_should_be_visible(self):
        self.book_demo_form_title.should(be.visible)

    @allure.step('Book Demo form title should have title {title}')
    def book_demo_form_title_should_have_correct_text(self, title):
        self.book_demo_form_title.should(have.exact_text(title))
