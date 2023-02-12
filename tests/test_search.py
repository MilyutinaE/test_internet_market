import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_and_components.components.login_component import Login_component
from pages_and_components.pages.main_page import Main_page
from pages_and_components.pages.product_page import Product_page

def test_search():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\pythonProject\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    main = Main_page(driver)
    main.authorization()
    time.sleep(1)  # без этой строчки  не нажимается поиск
    product_for_search = 'Мышь проводная Logitech Gaming Mouse G PRO HERO'
    main.search_product(product_for_search)
    time.sleep(1)
    product = Product_page(driver)
    product_name = product.get_product_name()
    print(product_name)
    is_product_right = product.is_product_right(product_name, product_for_search)
    print(is_product_right)
    assert is_product_right == True
    print("Названия товара из поиска и со страницы найденного товара совпадают")