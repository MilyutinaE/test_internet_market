import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_and_components.components.header_component import Header_component
from pages_and_components.pages.catalog_page import Catalog_page
from pages_and_components.pages.main_page import Main_page
from pages_and_components.pages.product_page import Product_page


# Открывается сайт, в левом меню клик на категорию, далее открывается первый товар в категории,
# проверяется есть ли у товара картинка, цена, рейтинг
def test_items_on_product_page(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\pythonProject\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    main = Main_page(driver)
    main.open_main_link()
    main.click_left_menu_toothbrush()
    time.sleep(2)
    catalog = Catalog_page(driver)
    catalog.product_click()

    product = Product_page(driver)

    # проверка, есть ли у товара картинка, цена, рейтинг
    have_image = product.have_image()
    have_price = product.have_price()
    have_rating = product.have_rating()
    try:
        assert have_image == True
        print("Картинки есть")
    except Exception as ex:
        print("Картинки нет")

    try:
        assert have_price == True
        print("Цена есть")
    except Exception as ex:
        print("Цены нет")

    try:
        assert have_rating == True
        print("Рейтинг есть")
    except Exception as ex:
        print("Рейтинга нет")

    driver.close()
