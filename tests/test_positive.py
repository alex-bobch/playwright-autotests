import pytest
from pages.quote_page import QuotePage


def test_valid_submission(page):
    quote_page = QuotePage(page)

    # Заполняем валидные данные
    quote_page.fill_form(
        name="John Doe",
        email="test@example.com",
        service="Service 1",
        message="Valid message with more than 5 chars"
    )
    quote_page.submit()

    # Проверяем успешную отправку
    l=quote_page.is_success()
    assert quote_page.is_success(),"Должно быть сообщение об успешной отправке формы"

def test_valid_submission_min(page):
    quote_page = QuotePage(page)

    # Заполняем валидные данные
    quote_page.fill_form(
        name="Alex Win",
        email="test1@example1.com",
        message="Valid message with more than 5 chars"
    )
    quote_page.submit()

    # Проверяем успешную отправку
    assert quote_page.is_success(),"Должно быть сообщение об успешной отправке формы"