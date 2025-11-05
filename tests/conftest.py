import pytest
from playwright.sync_api import Page, BrowserContext
import allure


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="ru-RU",
        timezone_id="Europe/Moscow"
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    
    # Установка таймаута по умолчанию
    page.set_default_timeout(30000)
    
    yield page
    
    # Скриншот при падении теста
    if page:
        try:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            pass
    
    page.close()


def pytest_configure(config):
    # Добавление кастомных маркеров
    config.addinivalue_line(
        "markers", "smoke: Mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: Mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "navigation: Mark test as navigation test"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        # Добавление информации о тесте в Allure
        if report.failed:
            allure.dynamic.label("status", "failed")
        elif report.passed:
            allure.dynamic.label("status", "passed")

