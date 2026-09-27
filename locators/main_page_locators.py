from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка для принятия cookies на главной странице
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    # Раздел "Вопросы о важном"
    SECTION_QUESTION_LOCATOR = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')

    # Локатор для вопросов
    @staticmethod
    def get_question_locator(number):
        return By.ID, f"accordion__heading-{number}"

    # Локатор для ответов
    @staticmethod
    def get_answer_locator(number):
        return By.ID, f"accordion__panel-{number}"

