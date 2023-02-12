from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_component(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login_user = 'pamiri6527@iucake.com'
    password_user = 'abebeb1111'

    # Локаторы для авторизации
    login_with_password = (By.XPATH, "//div[@class ='block-other-login-methods__password-caption']")
    username_input = (By.XPATH, "//*[@autocomplete='username']")
    password_input = (By.XPATH, "//*[@autocomplete='current-password']")
    login_button = (By.XPATH, "//*[@class='base-main-button']//*[contains(text(),'Войти')]")

    # Методы для авторизации
    def click_login_with_password(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login_with_password))
        _login = self.driver.find_element(*self.login_with_password)
        _login.click()
        print("Click login with password")

    def input_username(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.username_input))
        _username = self.driver.find_element(*self.username_input)
        _username.send_keys(self.login_user)
        print("Input username")

    def input_password(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.password_input))
        _password = self.driver.find_element(*self.password_input)
        _password.send_keys(self.password_user)
        print("Input password")

    def click_login_button(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login_button))
        _login_button = self.driver.find_element(*self.login_button)
        _login_button.click()
        print("Click login button")
