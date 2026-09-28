import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Принять куки, если кнопка "да все привыкли" отображается')
    def accept_cookies(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Проскроллить до раздела "Вопросы о важном"')
    def scroll_to_section(self):
        self.scroll_to_element(MainPageLocators.SECTION_QUESTION_LOCATOR)

    @allure.step('Нажать на вопрос')
    def click_to_question (self, number):
        locator_question = MainPageLocators.get_question_locator(number)
        self.click_to_element(locator_question)

    @allure.step('Получить ответ на вопрос')
    def check_answer(self, number):
        locator_answer = MainPageLocators.get_answer_locator(number)
        return self.get_text_from_element(locator_answer)
