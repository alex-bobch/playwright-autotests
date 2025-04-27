import pytest
from pages.quote_page import QuotePage


def test_invalid_submission(page):
    quote_page = QuotePage(page)
    quote_page.submit()
    # Заполняем невалидные данные
    quote_page.fill_form(
        name="",  # Пустое обязательное поле
        email="invalid-email",
        message="1234"  # Менее 5 символов
    )
    quote_page.submit()

    # Проверяем ошибки валидации
    assert not quote_page.is_success(),"Не должно быть сообщения об успешной отправке"
    assert quote_page.has_error("name"),"Поле должно быть помечено, как не валидное"
    assert quote_page.has_error("email"),"Поле должно быть помечено, как не валидное"
    assert quote_page.has_error("message"),"Поле должно быть помечено, как не валидное"

def test_invalid_submission_after_vaild(page):
    # отправляем валидную форму
    quote_page = QuotePage(page)
    quote_page.fill_form(
        name="Victor Green",
        email="test2-email@gmail.com",
        message="Тестовое сообщение"  # Менее 5 символов
    )
    quote_page.submit()
    # Заполняем невалидные данные
    quote_page.fill_form(
        name="",  # Пустое обязательное поле
        email="invalid-email",
        message="1234"  # Менее 5 символов
    )
    quote_page.submit()

    # Проверяем ошибки валидации
    assert not quote_page.is_success(),"Не должно быть сообщения об успешной отправке"
    assert quote_page.has_error("name"),"Поле должно быть помечено, как не валидное"
    assert quote_page.has_error("email"),"Поле должно быть помечено, как не валидное"
    assert quote_page.has_error("message"),"Поле должно быть помечено, как не валидное"