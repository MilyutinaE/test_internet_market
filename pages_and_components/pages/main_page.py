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


    url = 'https://doctorslon.ru/'


    # Локаторы


    # Методы



    def open_main_link(self):
        self.driver.get(self.url)
