import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_and_components.components.login_component import Login_component
from pages_and_components.components.cart_component import Cart_component
from pages_and_components.pages.main_page import Main_page
from pages_and_components.pages.product_page import Product_page
from pages_and_components.pages.cart_page import Cart_page

def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\pythonProject\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    main = Main_page(driver)
    main.authorization()
    time.sleep(3) # без этой строчки никак не получается нажать на кнопку войти
    main.click_login()
    login = Login_component(driver)
    login.click_login_with_password()
    login.input_username()
    login.input_password()
    login.click_login_button()
    time.sleep(1) # без этой строчки  не нажимается поиск
    product_for_search = 'Мышь проводная Logitech Gaming Mouse G PRO HERO'
    main.search_product(product_for_search)
    time.sleep(2)
    product = Product_page(driver)
    time.sleep(3)
    product.buy_product()
    time.sleep(2)
    cart = Cart_component(driver)
    cart.cart_click()
    cart_page = Cart_page(driver)
    cart_page.checkout_click()