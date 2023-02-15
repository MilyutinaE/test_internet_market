from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Catalog_search_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Локатор продукта в каталоге поиска
        self.product_in_search = (By.XPATH, "(//*[@class='digi-product__image'])[1]")
        self.wait_for_loading

    def first_product_click(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_in_search))
            _product = self.driver.find_element(*self.product_in_search)
            _product.click()
            print("Click  product")
        except Exception as ex:
            print("Товары не найдены")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_in_search))




