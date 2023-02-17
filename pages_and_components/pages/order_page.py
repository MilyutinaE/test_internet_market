import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class Order_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Локаторы
        self.make_order_button = (By.XPATH, "//*[contains(text(),'Оформить')]")
        self.wait_for_loading

    def make_order(self):
        with allure.step("Make order"):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.make_order_button))
            _make_order_button = self.driver.find_element(*self.make_order_button)
            _make_order_button.click()
            print("Click make order in order page (Нажать Оформить заказ на странице заказа)")


    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.make_order_button))


