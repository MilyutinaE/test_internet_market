import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    url = 'https://www.dns-shop.ru/'


    # Локаторы
    login = (By.XPATH, "//*[@class='personal-block-desktop']//*[@class='base-ui-button-v2__text']")
    search = (By.XPATH, "//*[@class='presearch__input']")

    # Методы
    def click_login(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login))
        _login = self.driver.find_element(*self.login)
        _login.click()
        print("Click login button")

    def search_product(self, product):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
        _search = self.driver.find_element(*self.search)
        _search.send_keys(product)
        _search.send_keys(Keys.RETURN)
        print("Search product")

    def authorization(self):
        self.driver.get(self.url)
