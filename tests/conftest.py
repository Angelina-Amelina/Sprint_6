import pytest
from selenium import webdriver
from urls import URL_MAIN_PAGE
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Firefox()
    browser.get(URL_MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    page.timeout = 10
    return page


@pytest.fixture(scope='function')
def order_page(driver):
    page = OrderPage(driver)
    page.timeout = 10
    return page
