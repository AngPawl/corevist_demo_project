import allure
from allure_commons.types import Severity

from corevist_demo_project.application import app


@allure.title('User successfully opens Watch Demo modal form')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_watch_demo_modal_form_successfully_pops_up():
    app.open()

    app.header_menu.open_watch_demo_modal_form()

    app.watch_demo_modal_form.should_have_correct_title('Watch Demo')


@allure.title('User successfully closes Watch Demo modal form')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_watch_demo_modal_form_successfully_closes():
    app.open()

    app.header_menu.open_watch_demo_modal_form()
    app.watch_demo_modal_form.close_by_clicking_on_close_button()

    app.watch_demo_modal_form.should_be_closed()
