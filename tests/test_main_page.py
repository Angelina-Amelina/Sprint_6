import allure
import pytest
from data import expected_answers

@allure.suite('Тесты главной страницы')
class TestMainPage:
    @allure.title('Проверка ответа из выпадающего списка.Вопрос №{number}')
    @allure.description('Тест проверяет, что при нажатии на "стрелочку" открывается соответствующий текст ответа')
    @pytest.mark.parametrize('number, answer', enumerate(expected_answers))
    def test_questions_and_answer(self, main_page, number, answer):
        main_page.accept_cookies()
        main_page.scroll_to_section()
        main_page.click_to_question(number)
        actual_answer = main_page.check_answer(number)
        assert actual_answer == answer
