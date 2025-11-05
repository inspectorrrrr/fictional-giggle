import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page):

        super().__init__(page)
        self.locators = MainPageLocators()
    
    @allure.step("Открыть главную страницу")
    def open(self):
        # Открыть главную страницу effective-mobile.ru
        self.navigate_to(self.locators.BASE_URL)
    
    @allure.step("Клик по ссылке 'О нас' в навигации")
    def click_about_link(self):
        # Используем get_by_role как в codegen
        self.page.get_by_role("link", name=self.locators.LINK_ABOUT_TEXT).click()
        # Ждем появление секции
        self.page.wait_for_timeout(500)
    
    @allure.step("Клик по ссылке 'Услуги' в навигации")
    def click_services_link(self):
        self.page.get_by_role("link", name=self.locators.LINK_SERVICES_TEXT).click()
        self.page.wait_for_timeout(500)
    
    @allure.step("Клик по ссылке 'Проекты' в навигации")
    def click_cases_link(self):

        self.page.get_by_role("link", name=self.locators.LINK_PROJECTS_TEXT).click()
        self.page.wait_for_timeout(500)
    
    @allure.step("Клик по ссылке 'Отзывы' в навигации")
    def click_reviews_link(self):
        self.page.get_by_role("link", name=self.locators.LINK_REVIEWS_TEXT).click()
        self.page.wait_for_timeout(500)
    
    @allure.step("Клик по ссылке 'Контакты' в навигации")
    def click_contacts_link(self):
        self.page.get_by_role("link", name=self.locators.LINK_CONTACTS_TEXT).click()
        self.page.wait_for_timeout(500)
    
    @allure.step("Проверить видимость секции 'О нас'")
    def is_about_section_visible(self) -> bool:
        try:
            section = self.page.locator(self.locators.SECTION_ABOUT_TEXT).get_by_text(
                self.locators.SECTION_ABOUT_TEXT_CONTENT
            )
            return section.is_visible(timeout=3000)
        except Exception:
            # Альтернативная проверка по тексту
            return self.page.get_by_text(self.locators.SECTION_ABOUT_TEXT_CONTENT, exact=True).first.is_visible(timeout=2000)
    
    @allure.step("Проверить видимость секции 'Услуги'")
    def is_services_section_visible(self) -> bool:
        try:
            return self.page.get_by_text(self.locators.SECTION_SERVICES_TEXT, exact=True).first.is_visible(timeout=3000)
        except Exception:
            # Fallback: проверка по ID секции
            section = self.page.locator(self.locators.SECTION_SERVICES).first
            return section.is_visible(timeout=2000)
    
    @allure.step("Проверить видимость секции 'Проекты'")
    def is_cases_section_visible(self) -> bool:
        try:
            section = self.page.locator(".t-slds__item.t-slds__item_active")
            return section.is_visible(timeout=3000)
        except Exception:
            try:
                return self.page.get_by_text("проекты", exact=False).first.is_visible(timeout=2000)
            except Exception:
                return False
    
    @allure.step("Проверить видимость секции 'Отзывы'")
    def is_reviews_section_visible(self) -> bool:
        try:
            return self.page.get_by_text(self.locators.SECTION_REVIEWS_TEXT).first.is_visible(timeout=3000)
        except Exception:
            section = self.page.locator(self.locators.SECTION_REVIEWS).first
            return section.is_visible(timeout=2000)
    
    @allure.step("Проверить видимость секции 'Контакты'")
    def is_contacts_section_visible(self) -> bool:
        try:
            return self.page.get_by_text(self.locators.SECTION_CONTACTS_TEXT, exact=True).first.is_visible(timeout=3000)
        except Exception:
            section = self.page.locator(self.locators.SECTION_CONTACTS).first
            return section.is_visible(timeout=2000)
    
    @allure.step("Проверить, что URL остался на главной странице")
    def verify_url_is_main_page(self):
        current_url = self.get_current_url()
        assert self.locators.BASE_URL in current_url, \
            f"URL должен содержать {self.locators.BASE_URL}, получен {current_url}"
    
    @allure.step("Проверить, что URL содержит якорь: {anchor}")
    def verify_url_contains_anchor(self, anchor: str):
        current_url = self.get_current_url()
        assert anchor in current_url, \
            f"URL должен содержать якорь '{anchor}', получен '{current_url}'"

