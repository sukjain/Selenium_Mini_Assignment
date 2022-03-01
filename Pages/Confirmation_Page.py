from selenium.webdriver.common.by import By


class confirmation():
    def __init__(self, driver):
        self.driver = driver

    def check_confirmation_msg(self):
        confirm = self.driver.find_element(By.XPATH, '// h2[text() = "PAYMENT SUCCESS"]').text
        assert confirm == "PAYMENT SUCCESS"
        print(confirm)

