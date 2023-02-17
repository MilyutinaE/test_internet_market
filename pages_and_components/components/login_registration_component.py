import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Login_registration_component(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.login_with_password = (By.XPATH, "//*[@class='form-login-sms']//*[@data-popup='email']")
        self.email_input = (By.XPATH, "//*[@name='login_email']")
        self.password_input = (By.XPATH, "//*[@name='login_password']")
        self.login_button = (By.XPATH, "//*[@value='Войти']")
        self.wait_for_loading


    # Методы для авторизации
    def click_login_with_password(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login_with_password))
        _login = self.driver.find_element(*self.login_with_password)
        _login.click()
        print("Click login with password")

    def input_email(self, login_user):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.email_input))
        _username = self.driver.find_element(*self.email_input)
        _username.send_keys(login_user)
        print("Input email")

    def input_password(self, password_user):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.password_input))
        _password = self.driver.find_element(*self.password_input)
        _password.send_keys(password_user)
        print("Input password")

    def click_login_button(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login_button))
        _login_btn = self.driver.find_element(*self.login_button)
        _login_btn.click()
        print("Click login button")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.login_with_password))

    def authorization(self, login_user, password_user):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.click_login_with_password()
            self.input_email(login_user)
            self.input_password(password_user)
            self.click_login_button()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
