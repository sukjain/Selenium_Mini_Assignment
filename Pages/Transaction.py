import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from Config.config import TestData


class Transaction():
    def __init__(self, driver):
        self.driver = driver

    def payment(self):

        self.driver.find_element(By.XPATH, '// span[text() = "Pay with Card"]').click()
        time.sleep(2)
        self.driver.switch_to.frame('stripe_checkout_app')

        self.driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(TestData.Email)

        for i in range(0,4):
            self.driver.find_element(By.ID, 'card_number').send_keys(TestData.Card_num)


        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@id="cc-exp"]').send_keys(TestData.date1)
        self.driver.find_element(By.XPATH, '//input[@id="cc-exp"]').send_keys(TestData.date2)

        self.driver.find_element(By.XPATH, '//input[@id="cc-csc"]').send_keys(TestData.Cvc)
        self.driver.find_element(By.XPATH, '  //input[ @ placeholder = "ZIP Code"]').send_keys(TestData.Postal_code)

        self.driver.find_element(By.XPATH, '//button[@id="submitButton"]').click()







