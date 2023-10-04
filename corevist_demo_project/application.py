import allure
from selene import browser

from corevist_demo_project.components.header_menu import HeaderMenu
from corevist_demo_project.components.live_chat import LiveChat
from corevist_demo_project.components.watch_demo_modal_form import WatchDemoModalForm
from corevist_demo_project.pages.about_page import AboutPage
from corevist_demo_project.pages.main_page import MainPage


class ApplicationManager:
    def __init__(self):
        self.main_page = MainPage()
        self.header_menu = HeaderMenu()
        self.live_chat = LiveChat()
        self.watch_demo_modal_form = WatchDemoModalForm()
        self.about_page = AboutPage()

    @staticmethod
    @allure.step('Open app')
    def open():
        browser.open('/')


app = ApplicationManager()
