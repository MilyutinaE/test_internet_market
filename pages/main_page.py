import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    main_url = 'https://www.dns-shop.ru/'

    # Locators

    login_personal_account = (By.XPATH, "//*[@class ='personal-block-desktop']//*[@class ='base-ui-button-v2__text']")

    login_popup = (By.XPATH, "//div[@class ='base-ui-button-v2__text'")

    # Methods

    def open_login(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_personal_account)))
        self.login_personal_account.click()










    add_product_1 = "//*[@id='add-to-cart-sauce-labs-backpack']"
    add_product_2 = "//*[@id='add-to-cart-sauce-labs-bike-light']"
    add_product_3 = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//*[@id='shopping_cart_container']"
    menu = "//*[@id='react-burger-menu-btn']"
    link_about = "//*[@id='about_sidebar_link']"

    # Getters - возвращают элементы






    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions
    def click_add_product_1(self):
        self.get_product_1().click()
        print("Click add product 1")

    def click_add_product_2(self):
        self.get_product_2().click()
        print("Click add product 2")


    def click_add_product_3(self):
        self.get_product_3().click()
        print("Click add product 3")


    def click_get_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click link about")


    # Methods
    def select_products_1(self):
        self.get_current_url()
        self.click_add_product_1()
        self.click_get_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_add_product_2()
        self.click_get_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_add_product_3()
        self.click_get_cart()


    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        # self.assert_url('https://saucelabs.com/')