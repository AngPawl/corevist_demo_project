import allure
from allure_commons.types import Severity

from corevist_demo_project.application import app


@allure.title('Button Scroll to Top works properly')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_scroll_button_returns_focus_to_the_top():
    app.open()

    app.main_page.scroll_to_mid_page_section().click_on_scroll_to_top_button()

    app.main_page.should_have_correct_title('B2B eCommerce for manufacturers on SAP.')
