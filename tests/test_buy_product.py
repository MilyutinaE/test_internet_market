import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages_and_components.components.header_component import Header_component
from pages_and_components.components.login_registration_component import Login_registration_component
from pages_and_components.pages.main_page import Main_page
from pages_and_components.pages.order_page import Order_page
from pages_and_components.pages.product_page import Product_page
from pages_and_components.pages.catalog_search_page import Catalog_search_page


@allure.description("test_buy_product- Открывается сайт, в  поиске ищется товар, далее выбирается первый товар из найденных."
                    " открываем его и смотрим,совпадает ли название товара, который искали. "
                    "потом кладем его в корзину, открываем корзину и переходим к оформлению")

def test_buy_product(set_up):
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

    # данные для авторизации
    login_user = 'fenova229@bk.ru'
    password_user = 'abebeb1111'

    login_registration.authorization(login_user, password_user)

    # товар для поиска
    product_for_search = 'curaprox enzycal 1450'

    header.input_search(product_for_search)
    time.sleep(2)
    driver.refresh() # без рефреша в автотесте не работает поиск. иногда не работает и с ним. нужно водить мышью по экрану
    driver.refresh()
    catalog_search = Catalog_search_page(driver)
    catalog_search.first_product_click()

    product = Product_page(driver)
    product_name = product.get_product_name().lower()

    product_name_correct = product_for_search in product_name

    assert product_name_correct == True
    print("Correct product name (продукт, который мы искали, совпадает с тем, который мы нашли")

    product.add_to_cart()

    product_name_popup = product.get_product_name_popup().lower()
    product_name_popup_correct = product_name in product_name_popup
    assert product_name_popup_correct == True
    print("Correct product name in popup (Название продукта на странице продукта совпадает с названием в модалке")

    product.make_order_popup()

    order = Order_page(driver)
    order.make_order()

    driver.close()

