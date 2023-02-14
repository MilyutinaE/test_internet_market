import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from pages_and_components.components.header_component import Header_component
from pages_and_components.components.login_registration_component import Login_registration_component
from pages_and_components.components.cart_component import Cart_component
from pages_and_components.pages.main_page import Main_page
from pages_and_components.pages.product_page import Product_page
from pages_and_components.pages.catalog_page import Catalog_page
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\pythonProject\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    main = Main_page(driver)
    main.open_main_link()

    header = Header_component(driver)
    header.click_login()

    login_registration = Login_registration_component(driver)
    login_registration.click_login_with_password()

    # данные для авторизации
    login_user = 'fenova229@bk.ru'
    password_user = 'abebeb1111'

    login_registration.input_email(login_user)
    login_registration.input_password(password_user)
    login_registration.click_login_button()

    # товар для поиска
    product_for_search = 'curaprox enzycal 1450'

    header.input_search(product_for_search)
    driver.refresh()

    catalog = Catalog_page(driver)
    catalog.first_product_click()

    product = Product_page(driver)
    product_name = product.get_product_name().lower()

    product_name_correct = product_for_search in product_name

    assert product_name_correct == True
    print("Correct product name (продукт, который мы искали, совпадает с тем, который мы нашли")



    # product = Product_page(driver)
    #
    # product.buy_product()
    #
    # cart = Cart_component(driver)
    # cart.cart_click()
    # cart_page = Cart_page(driver)
    # cart_page.checkout_click()