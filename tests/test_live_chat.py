import allure
from allure_commons.types import Severity

from corevist_demo_project.application import app


@allure.title('User successfully opens Live Chat')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_live_chat_successfully_opens():
    app.open()

    app.live_chat.open_chat_box()

    app.live_chat.opened_chat_box_header_should_contain_company_name('Corevist')
