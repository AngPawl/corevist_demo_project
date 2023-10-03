import allure
from selene import browser

from corevist_demo_project.components.header_menu import HeaderMenu
from corevist_demo_project.components.watch_demo_modal_form import WatchDemoModalForm
from corevist_demo_project.pages.about_page import AboutPage
from corevist_demo_project.pages.main_page import MainPage
from corevist_demo_project.pages.request_a_demo_page import RequestADemoPage


class ApplicationManager:
    def __init__(self):
        self.main_page = MainPage()
        self.header_menu = HeaderMenu()
        self.request_a_demo_page = RequestADemoPage()
        self.watch_demo_modal_form = WatchDemoModalForm()
        self.about_page = AboutPage()

    @staticmethod
    @allure.step('Open app')
    def open():
        browser.open('/')


app = ApplicationManager()
