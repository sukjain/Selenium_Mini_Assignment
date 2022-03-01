from selenium.webdriver.common.by import By
from selenium import webdriver
class Moisturizers():

    def __init__(self, driver):
        self.driver=driver

    def product_click(self, text2):
        print("Buy Moisturizers")
        data = self.driver.find_elements(By.XPATH, '//p[@class="font-weight-bold top-space-10"]')
        Add = self.driver.find_element(By.XPATH, '//button[text()="Add"]')
        for i in data:
            data1 = i.text
            if (data1.__contains__(text2)):
                Add.click()
                print(data1)
                break;



    def click_on_cart(self):
        self.driver.find_element(By.XPATH, '// button[ @ onclick = "goToCart()"]').click()


