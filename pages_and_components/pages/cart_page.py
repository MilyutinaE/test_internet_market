from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    checkout_button = (By.XPATH, "//*[@id='buy-btn-main']")

    def checkout_click(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.checkout_button))
        _checkout_button = self.driver.find_element(*self.checkout_button)
        _checkout_button.click()
        print("Click checkout (Перейти к оформлению заказ)  ")




