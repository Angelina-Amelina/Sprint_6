from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    # Переходим по url в браузере
    def follow_url(self, url):
        self.driver.get(url)

    # Ждем появления элемента на странице и возвращаем его
    def find_element_with_wait(self, locator):
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Ждем пока элемент станет кликабельным и кликаем на него
    def click_to_element(self, locator):
        self.wait.until(
            expected_conditions.element_to_be_clickable(locator)).click()

    # Ждем появления текста внутри элемента
    def wait_text(self, locator, text):
        self.wait.until(
            expected_conditions.text_to_be_present_in_element_value(locator, text))

    # Ждем пока элемент станет видимым и возвращаем его текст
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)

        return element.text
    # Скроллим страницу до нужного элемента
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Ждем появления поля ввода, очищаем его и вводим переданный текст
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

   # Ждем пока браузер сменит переключит на нужный домен
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            lambda driver: "ya.ru" in driver.current_url or "dzen.ru" in driver.current_url
        )
   # Проверяем текущий URL страницы
    def get_current_url(self):
        return self.driver.current_url

   # Поиск списка элементов
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)