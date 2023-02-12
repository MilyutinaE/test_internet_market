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
    product_name = (By.XPATH, "//*[@class='product-card-top__title']")
    buy_button = (By.XPATH, "//*[@class='product-card-top__buy']//*[contains(text(),'Купить')]")

    # Методы
    def get_product_name(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_name))
        _product_name = self.driver.find_element(*self.product_name).text

        return _product_name

    # Метод, который проверяет, что продукт, который искали, соответствует продукту, на страниц
    def is_product_right(self, product_name, product_search):
        product_right = product_search in product_name
        return product_right

    def buy_product(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.buy_button))
        _buy_product = self.driver.find_element(*self.buy_button)
        _buy_product.click()
        print("Click buy button")
