from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Кнопка для принятия cookies на главной странице
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    # Кнопка "Заказать" в хэдере на главной странице
    BUTTON_ORDER_HEADER = (By.XPATH, '//button[text()="Заказать"]')
    # Поле "Имя" на странице заказов
    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "* Имя"]')
    # Поле "Фамилия" на странице заказов
    SURNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "* Фамилия"]')
    # Поле "Адрес: куда привезти заказ" на странице заказов
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "* Адрес: куда привезти заказ"]')
    # Поле выбора станции метро из выпадающего списка
    METRO_SELECT = (By.CSS_SELECTOR, 'input[placeholder = "* Станция метро"]')
    # Выбор метро из списка
    METRO_OPTION = (By.XPATH, '//ul[contains(@class, "select-search__options")]//div[text()="Преображенская площадь"]')
    # Поле для заполнения номера телефона
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "* Телефон: на него позвонит курьер"]')
    # Кнопка "Далее"
    BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]')

    # Поле "Когда привезти самокат"
    DELIVER_ORDER = (By.CSS_SELECTOR, 'input[placeholder = "* Когда привезти самокат"]')
    # Поле выбора срока аренды
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    # Поле выбора срока аренды - сутки
    RENT_DURATION_ONE_DAY = (By.XPATH, '//div[@class="Dropdown-menu"]/div[text()="сутки"]')
    # Поле выбора срока аренды - двое суток
    RENT_DURATION_TWO_DAYS = (By.XPATH, '//div[@class="Dropdown-menu"]/div[text()="двое суток"]')
    # Заголовок "Про аренду"
    RENT_HEADER = (By.XPATH, '//div[text()="Про аренду"]')
    # Выбор дня в календаре
    CALENDAR_SELECTED_DAY = (By.CSS_SELECTOR, '.react-datepicker__day:not([class*="disabled"])')
    # Поле выбора цвета самоката
    COLOR_ORDER = (By.XPATH, '//div[div[text()="Цвет самоката"]]')
    # Чекбокс для "черный жемчуг"
    COLOR_BLACK_ORDER = (By.XPATH, '// input[@id = "black"]')
    # Чекбокс для "серая безысходность"
    COLOR_GREY_ORDER = (By.XPATH, '// input[@id ="grey"]')
    # Поле "Комментарий для курьера"
    COMMENT_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "Комментарий для курьера"]')
    # Кнопка "Назад"
    BUTTON_BACK = (By.XPATH, '//button[text()="Назад"]')
    # Кнопка "Заказать"
    BUTTON_ORDER_RENTAL_PAGE = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[text()="Заказать"]')

    # Модальное окно "Хотите оформить заказ?"
    MODAL_CONFIRMATION_ORDER = (By.XPATH, '//div[contains(@class, "Order_Modal__")]')
    # Кнопка "Да" в модальном окне
    BUTTON_YES_MODAL = (By.XPATH, '//div[contains(@class, "Order_Modal__")]//button[text()="Да"]')
    # Кнопка "Нет" в модальном окне
    BUTTON_NO_MODAL = (By.XPATH, '//div[contains(@class, "Order_Modal__")]//button[text()="Нет"]')

    # Модальное окно "Заказ оформлен"
    MODAL_SUCCESS_ORDER = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
    # Кнопка "Посмотреть статус"
    BUTTON_STATUS_ORDER = (By.XPATH, '//button[text()="Посмотреть статус"]')

    # Кнопка "Отменить заказ" на странице успешно оформленного и отслеживаемого заказа
    BUTTON_CANCEL_ORDER = (By.XPATH, '//button[text()="Отменить заказ"]')
    # Статус заказа на странице заказа
    PAGE_STATUS_ORDER = (By.XPATH, '//div[text()="Самокат на складе"]')

    # Кнопка "Заказать" в середине страницы
    BUTTON_ORDER_BODY = (By.XPATH, '//button[text()="Заказать"]')