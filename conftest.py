import pytest
import os

def is_visible_mode():
    """Определяем режим с приоритетом для переменной окружения"""
    env_value = os.getenv("PLAYWRIGHT_HEADLESS", "false").lower()
    return env_value in ("false", "0", "no")


@pytest.fixture(scope="function", params=["chromium", "firefox"])
def browser(request, playwright):
    browser_name = request.param
    launch_options = {
        "headless": not is_visible_mode(),  # Инвертируем логику
        "slow_mo": 1000 if is_visible_mode() else 0,
        "timeout": 60000
    }

    browser = getattr(playwright, browser_name).launch(**launch_options)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.goto("https://qatest.datasub.com/quote.html", wait_until="networkidle")

    # Явное ожидание и скриншот для отладки
    page.wait_for_selector("#quoteForm", state="visible", timeout=15000)
    if is_visible_mode():
        page.screenshot(path=f"debug-{browser.browser_type.name}.png")

    yield page
    page.close()