import allure
from Locators.LoginLocators import PathForLogin
from selenium.webdriver.common.by import By


class LoginPageFunc:

    def __init__(self, driver):
        self.driver = driver
        self.email_ = PathForLogin.email_
        self.pass_ = PathForLogin.pass_
        self.click_ = PathForLogin.click_
        self.login_ = PathForLogin.login_


    @allure.step
    def Click_func(self):
        self.driver.find_element(By.XPATH,self.login_).click()

    @allure.step
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_).clear()
        self.driver.find_element(By.XPATH,self.email_).send_keys(email)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.pass_).clear()
        self.driver.find_element(By.XPATH,self.pass_).send_keys(password)

    @allure.step
    def click_Login(self):
        self.driver.find_element(By.XPATH,self.click_).click()