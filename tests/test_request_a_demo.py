import allure
from allure_commons.types import Severity

from corevist_demo_project.application import app


@allure.title('User successfully opens Request a Demo page')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_request_a_demo_page_successfully_opens():
    app.open()

    app.main_page.open_request_a_demo_page()

    app.request_a_demo_page.book_demo_form_title_should_be_visible()
    app.request_a_demo_page.book_demo_form_title_should_have_correct_text(
        'Book Your Custom Demo'
    )
