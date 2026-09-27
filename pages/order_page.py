import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.logo_page_locators import LogoPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step('Принять куки, если кнопка "да все привыкли" отображается')
    def accept_cookies(self):
        self.click_to_element(OrderPageLocators.COOKIE_BUTTON)
    @allure.step('Нажать на кнопку "Заказать" в хэдере главной страницы')
    def click_header_order_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_HEADER)
    @allure.step('Проскроллить до кнопки "Заказать" в середине главной страницы')
    def click_body_order_button(self):
        button_body = self.find_element_with_wait(OrderPageLocators.BUTTON_ORDER_BODY)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_body)
        buttons = self.driver.find_elements(*OrderPageLocators.BUTTON_ORDER_BODY)
        buttons[1].click()
    @allure.step('Заполнить форму "Кому заказать" и нажать на кнопку "Далее"')
    def fill_user_data(self, name, surname, address, phone):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_to_element(OrderPageLocators.METRO_SELECT)
        self.click_to_element(OrderPageLocators.METRO_OPTION)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, phone)

        self.click_to_element(OrderPageLocators.BUTTON_NEXT)
        self.find_element_with_wait(OrderPageLocators.DELIVER_ORDER)
    @allure.step('Заполнить форму "Про аренду" и нажать на кнопку "Заказать"')
    def fill_rent_data(self, date, comment):
        self.add_text_to_element(OrderPageLocators.DELIVER_ORDER, date)
        self.find_element_with_wait(OrderPageLocators.DELIVER_ORDER).send_keys(Keys.ENTER)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENT_DURATION_ONE_DAY)
        self.click_to_element(OrderPageLocators.COLOR_GREY_ORDER)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, comment)

        self.click_to_element(OrderPageLocators.BUTTON_ORDER_RENTAL_PAGE)
    @allure.step('Нажать "Да" в модальном окне "Хотите оформить заказ?"')
    def click_modal_success(self):
        self.click_to_element(OrderPageLocators.BUTTON_YES_MODAL)
    @allure.step('Проверить отображение всплывающего окна с сообщением об успешном создании заказа')
    def modal_order_successful(self):
        return self.find_element_with_wait(OrderPageLocators.MODAL_SUCCESS_ORDER).is_displayed()
    @allure.step('Кликнуть на лого "Самокат"')
    def click_scooter_logo(self):
        self.click_to_element(LogoPageLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть на лого "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(LogoPageLocators.LOGO_YANDEX)
