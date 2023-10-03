import allure
from allure_commons.types import Severity

from corevist_demo_project.application import app


@allure.title('Header Menu has the correct titles')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_menu_has_correct_titles():
    app.open()

    app.header_menu.should_have_correct_titles(
        [
            'Platform',
            'Solutions',
            'Pricing',
            'Results',
            'Resources',
            'Partners',
            'Company',
        ]
    )


@allure.title('Header Menu has the logo')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_menu_has_logo():
    app.open()

    app.header_menu.logo_should_be_present()


@allure.title('User opens a selected page via Header Menu')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_open_selected_page_via_header_menu():
    app.open()

    app.header_menu.open_selected_page('Company')

    app.about_page.should_have_correct_title('About Corevist')
