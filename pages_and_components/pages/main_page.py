from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure



class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Локаторы
        self.left_menu_toothbrush =  (By.XPATH, "//*[@class='category-item_text' and contains(text(),'Зубные щетки')]")


    url = 'https://doctorslon.ru/'

    # Методы
    def click_left_menu_toothbrush(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.left_menu_toothbrush))
        _login_btn = self.driver.find_element(*self.left_menu_toothbrush)
        _login_btn.click()
        print("Click left menu toothbrush")



    def open_main_link(self):
        with allure.step("Open main page"):
            self.driver.get(self.url)
