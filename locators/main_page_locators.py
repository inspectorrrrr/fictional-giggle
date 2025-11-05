class MainPageLocators:

    BASE_URL = "https://effective-mobile.ru"
    
    NAV_ABOUT = "a[href='#about']"
    NAV_SERVICES = "a[href='#moreinfo']"
    NAV_CASES = "a[href*='case'], a:has-text('Кейсы')"
    NAV_REVIEWS = "a[href='#Reviews']"
    NAV_CONTACTS = "a[href='#contacts']"
    
    SECTION_ABOUT = "#about"
    SECTION_SERVICES = "#moreinfo"
    SECTION_CASES = "[id*='case'], [id*='project']"
    SECTION_REVIEWS = "#Reviews"
    SECTION_CONTACTS = "#contacts"
    

    SECTION_ABOUT_TN_ATOM = "div.tn-atom[field='tn_text_1680508197707']"

    SECTION_SERVICES_TN_ATOM = "div.tn-atom[field*='service'], div.tn-atom:has-text('Услуги')"

    SECTION_REVIEWS_TN_ATOM = "div.tn-atom:has-text('ОТЗЫВЫ'), div.tn-atom:has-text('Отзывы')"

    SECTION_CONTACTS_TN_ATOM = "div.tn-atom[field*='contact'], div.tn-atom:has-text('контакты')"
    

    LOGO = "a:has-text('Effective Mobile')"
    MAIN_HEADING = "h1"
    

    LINK_ABOUT_TEXT = "[ О нас ]"
    LINK_SERVICES_TEXT = "[ Услуги ]"
    LINK_PROJECTS_TEXT = "[ Проекты ]"
    LINK_REVIEWS_TEXT = "[ Отзывы ]"
    LINK_CONTACTS_TEXT = "[ Контакты ]"
    
    SECTION_ABOUT_TEXT = "#rec572359627"
    SECTION_ABOUT_TEXT_CONTENT = "О нас"
    SECTION_SERVICES_TEXT = "услуги"
    SECTION_REVIEWS_TEXT = "ОТЗЫВЫ КЛИЕНТОВ"
    SECTION_CONTACTS_TEXT = "контакты"

