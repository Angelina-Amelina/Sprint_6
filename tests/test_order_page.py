import allure
import pytest
from urls import URL_MAIN_PAGE, URL_YANDEX_DZEN
from data import user_data_single, user_data_two

@allure.suite('Тесты заказа самоката')
class TestOrderPage:
    @allure.title('Проверка заказа товара двумя способами через кнопку "Заказать"')
    @allure.description('Тест проверяет возможность заказа самоката двумя способами')
    @pytest.mark.parametrize("name, surname, address, phone, date, comment", user_data_single)
    def test_order_flow_from_header(self, order_page, name, surname, address, phone, date, comment):
        order_page.click_header_order_button()
        order_page.fill_user_data(name, surname, address, phone)
        order_page.fill_rent_data(date, comment)
        order_page.click_modal_success()

        assert order_page.modal_order_successful()

    @allure.title('Проверка заказа товара через кнопку "Заказать" в середине страницы')
    @pytest.mark.parametrize("name, surname, address, phone, date, comment", user_data_two)
    def test_order_flow_from_body(self, order_page, name, surname, address, phone, date, comment):
        order_page.accept_cookies()
        order_page.click_body_order_button()
        order_page.fill_user_data(name, surname, address, phone)
        order_page.fill_rent_data(date, comment)
        order_page.click_modal_success()

        assert order_page.modal_order_successful()

    @allure.title('Проверка перехода на главную страницу Яндекс.Самоката')
    def test_scooter_logo_redirect(self, order_page):
        order_page.click_header_order_button()
        order_page.click_scooter_logo()

        assert order_page.get_current_url() == URL_MAIN_PAGE

    @allure.title('Проверка перехода на главную страницу Яндекс.Дзена')
    def test_yandex_logo_redirect(self, order_page):
        order_page.click_yandex_logo()
        order_page.switch_to_new_window()

        assert URL_YANDEX_DZEN in order_page.get_current_url()
