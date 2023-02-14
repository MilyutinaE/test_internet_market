from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class Product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Локаторы
        self.product_name = (By.XPATH, "//*[@class='product-title']//*[@itemprop='name']")
        self.wait_for_loading

    def get_product_name(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_name))
        _product_name = self.driver.find_element(*self.product_name).text
        return _product_name

    def checkout_click(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.checkout_button))
        _checkout_button = self.driver.find_element(*self.checkout_button)
        _checkout_button.click()
        print("Click checkout (Перейти к оформлению заказ)  ")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_name))


