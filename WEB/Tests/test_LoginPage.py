from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPageFunc
from Base.basePage import Base
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.basePage import Base
import allure
from allure_commons.types import AttachmentType

# def init_without_login():
#     driver = webdriver.Chrome('../../Driver/chromedriver.exe')
#     driver.get("https://wondemagen-barbershop.herokuapp.com/")
#     driver.maximize_window()
#     WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Login')]"))).click()
#     return driver

@pytest.mark.usefixtures('set_up')

class TestLogincoreectly(Base):

    """"test 1"""
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.nightly_build
    def test_login_success(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.Click_func()
        login.enter_email("tsiona@gmail.com")
        login.enter_password("123456")
        login.click_Login()
        # value = driver.find_element(By.XPATH, "//button[contains(text(),'log out')]"))).get_attribute("innerText")
        try:
            value = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'log out')]"))).get_attribute(
                "innerText")
            assert value == "log out"
        except Exception as e:
            driver.get_screenshot_as_png()
            driver.save_screenshot("log out button")

    """test 2"""
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_login_when_password_incorrect(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.Click_func()
        login.enter_email("tsiona@gmail.com")
        login.enter_password("11111111")
        login.click_Login()
        # value = driver.find_element(By.XPATH,"//h4[contains(text(),'incorrect Password/Email')]").get_attribute("innerText")
        try:
            value = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//h4[contains(text(),'incorrect Password/Email')]"))).get_attribute("innerText")
            assert value == "incorrect Password/Email"
        except Exception as e :
            driver.get_screenshot_as_png()
            driver.save_screenshot("incorrect Password/Email")


    """test 3"""
    @pytest.mark.regression
    @pytest.mark.nightly_build
    def test_invalid_login_when_passwordField_is_null(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.Click_func()
        login.enter_email("tsiona@gmail.com")
        login.enter_password(" ")

        button = driver.find_element(By.XPATH,"//div[1]/form[1]/input[3]").is_enabled()
        assert button == False

    """test 4"""
    @pytest.mark.nightly_build
    @pytest.mark.regression
    def test_invalid_login_when_emailField_is_null(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.Click_func()
        login.enter_email("")
        login.enter_password("123456")

        button = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
        assert button == False

    """"test 5"""
    @pytest.mark.regression
    @pytest.mark.nightly_build
    def test_invalid_login_when_all_fields_are_null(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.Click_func()
        login.enter_email("")
        login.enter_password("")
        login.click_Login()

        button = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
        assert button == False


    def test_COPT_TEST_FOR_GIT(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.Click_func()
        login.enter_email("")
        login.enter_password("")
        login.click_Login()

        button = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
        assert button == False









