from selenium.webdriver.common.by import By

class LogoPageLocators:
    # Лого "Самокат"
    LOGO_SCOOTER = (By.XPATH, '//a[@href="/"]')
    # Лого "Яндекс"
    LOGO_YANDEX = (By.XPATH, '//a[contains(@href, "ya.ru")]')


