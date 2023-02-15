from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Catalog_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Локатор продукта в каталоге поиска
        self.product = (By.XPATH, "(//*[@class='product-data_title'])[1]")
        self.wait_for_loading

    def product_click(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product))
            _product = self.driver.find_element(*self.product)
            _product.click()
            print("Click  product")
        except Exception as ex:
            print("Товаров нет")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product))




