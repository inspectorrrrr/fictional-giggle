import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Навигация на главной странице")
@allure.story("Проверка переходов по блокам")
class TestMainPageNavigation:        
    @allure.title("Тест перехода к блоку 'О нас'")
    @allure.description("Проверка клика по ссылке 'О нас' и перехода к соответствующей секции")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_about_section(self, page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть по ссылке 'О нас'"):
            main_page.click_about_link()
        
        with allure.step("Проверить URL с якорем '#about'"):
            main_page.verify_url_contains_anchor("#about")
        
        with allure.step("Проверить, что секция 'О нас' видима"):
            assert main_page.is_about_section_visible(), \
                "Секция 'О нас' должна быть видимой после клика"
        
        with allure.step("Сделать скриншот секции"):
            main_page.take_screenshot("about_section")
    
    @allure.title("Тест перехода к блоку 'Услуги'")
    @allure.description("Проверка клика по ссылке 'Услуги' и перехода к соответствующей секции")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_services_section(self, page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть по ссылке 'Услуги'"):
            main_page.click_services_link()
        
        with allure.step("Проверить URL с якорем '#moreinfo'"):
            main_page.verify_url_contains_anchor("#moreinfo")
        
        with allure.step("Проверить, что секция 'Услуги' видима"):
            assert main_page.is_services_section_visible(), \
                "Секция 'Услуги' должна быть видимой после клика"
        
        with allure.step("Сделать скриншот секции"):
            main_page.take_screenshot("services_section")
    
    @allure.title("Тест перехода к блоку 'Проекты'")
    @allure.description("Проверка клика по ссылке 'Проекты' и перехода к соответствующей секции")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_cases_section(self, page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть по ссылке 'Проекты'"):
            main_page.click_cases_link()
        
        # Для Проектов проверка URL может быть разной, так как это может быть слайдер
        # Проверяем видимость секции
        with allure.step("Проверить, что секция 'Проекты' видима"):
            assert main_page.is_cases_section_visible(), \
                "Секция 'Проекты' должна быть видимой после клика"
        
        with allure.step("Сделать скриншот секции"):
            main_page.take_screenshot("projects_section")
    
    @allure.title("Тест перехода к блоку 'Отзывы'")
    @allure.description("Проверка клика по ссылке 'Отзывы' и перехода к соответствующей секции")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_reviews_section(self, page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть по ссылке 'Отзывы'"):
            main_page.click_reviews_link()
        
        with allure.step("Проверить URL с якорем '#Reviews'"):
            main_page.verify_url_contains_anchor("#Reviews")
        
        with allure.step("Проверить, что секция 'Отзывы' видима"):
            assert main_page.is_reviews_section_visible(), \
                "Секция 'Отзывы' должна быть видимой после клика"
        
        with allure.step("Сделать скриншот секции"):
            main_page.take_screenshot("reviews_section")
    
    @allure.title("Тест перехода к блоку 'Контакты'")
    @allure.description("Проверка клика по ссылке 'Контакты' и перехода к соответствующей секции")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_contacts_section(self, page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть по ссылке 'Контакты'"):
            main_page.click_contacts_link()
        
        with allure.step("Проверить URL с якорем '#contacts'"):
            main_page.verify_url_contains_anchor("#contacts")
        
        with allure.step("Проверить, что секция 'Контакты' видима"):
            assert main_page.is_contacts_section_visible(), \
                "Секция 'Контакты' должна быть видимой после клика"
        
        with allure.step("Сделать скриншот секции"):
            main_page.take_screenshot("contacts_section")
    
    @allure.title("Тест последовательной навигации по всем блокам")
    @allure.description("Проверка последовательного перехода по всем секциям страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_through_all_sections(self, page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        sections = [
            ("О нас", main_page.click_about_link, main_page.is_about_section_visible),
            ("Услуги", main_page.click_services_link, main_page.is_services_section_visible),
            ("Проекты", main_page.click_cases_link, main_page.is_cases_section_visible),
            ("Отзывы", main_page.click_reviews_link, main_page.is_reviews_section_visible),
            ("Контакты", main_page.click_contacts_link, main_page.is_contacts_section_visible),
        ]
        
        for section_name, click_method, visibility_method in sections:
            with allure.step(f"Переход к секции '{section_name}'"):
                click_method()
                assert visibility_method(), \
                    f"Секция '{section_name}' должна быть видимой"
                main_page.take_screenshot(f"section_{section_name.lower()}")

