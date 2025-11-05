import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):

        self.page = page
    
    @allure.step("Открыть URL: {url}")
    def navigate_to(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")
    
    @allure.step("Клик по элементу: {locator}")
    def click(self, locator: str):
        self.page.locator(locator).click()
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
    
    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.page.url
    
    @allure.step("Проверить, что URL содержит: {expected_url}")
    def assert_url_contains(self, expected_url: str):
        current_url = self.get_current_url()
        assert expected_url in current_url, \
            f"Ожидается URL содержащий '{expected_url}', получен '{current_url}'"
    
    @allure.step("Ждать элемент: {locator}")
    def wait_for_element(self, locator: str, timeout: int = 10000):
        self.page.wait_for_selector(locator, timeout=timeout)
    
    @allure.step("Скроллить к элементу: {locator}")
    def scroll_to_element(self, locator: str):
        self.page.locator(locator).scroll_into_view_if_needed()
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
    
    @allure.step("Сделать скриншот: {name}")
    def take_screenshot(self, name: str = "screenshot"):
        screenshot_bytes = self.page.screenshot(full_page=True)
        allure.attach(
            screenshot_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

