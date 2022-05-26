import allure
import pytest
from Tests.test_LoginPage import test_login_success

from Locators.ReviewLocators import PathForReview
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('set-up')
class TestReview:

    def __init__(self,driver):
        self.driver=driver
        self.BarberNamefiled = PathForReview.BarberNamefiled
        self.PresonName = PathForReview.PresonName
        self.ReviewComment = PathForReview.ReviewComment
        self.ButtonSendReview = PathForReview.ButtonSendReview

    @allure.step
    def EnterReviewPage(self,driver):
        self.driver.get("https://wondemagen-barbershop.herokuapp.com/Review")

    @allure.step
    def EnterBarberName(self,driver):
        self.driver.find_element(By.XPATH,self.BarberNamefiled).send_keys("aviel")

    @allure.step
    def EnterPersonName(self,driver):
        self.driver.find_element(By.XPATH,self.EnterPersonName).send_keys("oshrat")

    @allure.step
    def EnterReview(self,driver):
        self.driver.find_element(By.XPATH,self.ReviewComment).send_keys("horrible haircut")

    @allure.step
    def ButtonSendReview(self,driver):
        self.driver.find_element(By.XPATH,self.ButtonSendReview).click()













