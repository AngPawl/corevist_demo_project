import allure
from selene import browser, have, be
from selene.support.conditions.have import exact_text


class HeaderMenu:
    def __init__(self):
        self.logo = browser.element('[class$="standard-logo"]')
        self.menu_titles = browser.all('.fusion-main-menu a.mega-menu-link[href$="/"]')
        self.watch_demo_button = browser.all('.mega-menu-link[href^="#"]').element_by(
            exact_text('WATCH DEMO')
        )

    @allure.step('Open {page_name} page')
    def open_selected_page(self, page_name):
        self.menu_titles.element_by(exact_text(page_name)).click()

    @allure.step('Open Watch Demo modal form')
    def open_watch_demo_modal_form(self):
        self.watch_demo_button.click()

    @allure.step('Header menu should has correct titles: {titles}')
    def should_have_correct_titles(self, titles):
        self.menu_titles.should(have.exact_texts(titles))

    @allure.step('Logo should be present on the page')
    def logo_should_be_present(self):
        self.logo.should(be.present)
