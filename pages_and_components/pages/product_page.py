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
        self.add_to_cart_button = (By.XPATH, "//*[@id='add_to_cart']")
        self.product_popup = (By.XPATH,"//*[@class='added-item_title']")
        self.make_order_popup_button = (By.XPATH, "//*[contains(text(),'Оформить')]")
        self.price = (By.XPATH, "//*[@itemprop='price']")
        self.rating = (By.XPATH, "//*[@itemprop='aggregateRating']")
        self.image = (By.XPATH, "//*[@itemprop='image']")
        self.wait_for_loading

    def get_product_name(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_name))
        _product_name = self.driver.find_element(*self.product_name).text
        return _product_name

    def add_to_cart(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.add_to_cart_button))
        _add_to_cart_button = self.driver.find_element(*self.add_to_cart_button)
        _add_to_cart_button.click()
        print("Add to cart (Нажать В корзину)")

    def get_product_name_popup(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_popup))
        _product_name = self.driver.find_element(*self.product_popup).text
        return _product_name

    def make_order_popup(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.make_order_popup_button))
        _make_order_popup_button = self.driver.find_element(*self.make_order_popup_button)
        _make_order_popup_button.click()
        print("Click make order in popup (Нажать Оформить заказ в модалке)")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_name))

    def have_image(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.image))
            _image = self.driver.find_element(*self.image)
            have = True
            return have
        except Exception as ex:
            print("Картинки нет")
            have = False
            return have

    def have_price(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.price))
            _price = self.driver.find_element(*self.price)
            have = True
            return have
        except Exception as ex:
            print("Картинки нет")
            have = False
            return have

    def have_rating(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.rating))
            _rating = self.driver.find_element(*self.rating)
            have = True
            return have
        except Exception as ex:
            print("Картинки нет")
            have = False
            return have