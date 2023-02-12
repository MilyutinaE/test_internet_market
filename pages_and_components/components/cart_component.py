from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class Cart_component(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    cart_button = (By.XPATH, "//*[@class='cart-button']")

    def cart_click(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.cart_button))
        _cart_click = self.driver.find_element(*self.cart_button)
        _cart_click.click()
        print("Click cart")




