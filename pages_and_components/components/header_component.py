from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

class Header_component(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Локаторы
        self.login = (By.XPATH, "//*[@class='header-main ']//*[@data-popup='phone']")
        self.search = (By.XPATH, "//*[@id='title-search-input']")
        self.all_results_button = (By.XPATH, "//*[@class='icon icon-search']")
        self.wait_for_loading


    def click_login(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login))
        _login_button = self.driver.find_element(*self.login)
        _login_button.click()
        print("Click login button (Профиль)")

    # Метод - найти товар в поиске
    def input_search(self, product):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
        _search = self.driver.find_element(*self.search)
        _search.send_keys(product)

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.all_results_button))
        _search_all = self.driver.find_element(*self.all_results_button)
        _search_all.click()

        print("Find products in search")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login))





