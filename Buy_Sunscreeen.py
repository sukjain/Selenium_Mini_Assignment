from selenium.webdriver.common.by import By


class Sunscreen():
    def __init__(self, driver):
        self.driver=driver


    def product_click_Sunscren(self, text3):
        print("Buy Sunscreen")
        data = self.driver.find_elements(By.XPATH, '//p[@class="font-weight-bold top-space-10"]')
        Add = self.driver.find_element(By.XPATH, '//button[text()="Add"]')
        for i in data:
            data1 = i.text
            if (data1.__contains__(text3)):
                Add.click()
                print(data1)
                break;




    def click_on_cart_sun(self):

        self.driver.find_element(By.XPATH, '// button[ @ onclick = "goToCart()"]').click()



