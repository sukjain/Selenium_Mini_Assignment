import time
import unittest
from selenium import webdriver

from Config.config import TestData
from Pages.Buy_Moisturizers import Moisturizers
from Pages.Buy_Sunscreeen import Sunscreen
from Pages.Confirmation_Page import confirmation
from Pages.Home_Page import HomePage
from Pages.Transaction import Transaction


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=TestData.Chrome_Executable_Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_homepage(self):
        driver = self.driver
        driver.get(TestData.Base_url)
        home = HomePage(driver)
        temp_value= home.get_temp()
        convert_temp = home.convert_into_int(temp_value)
        print("Current Temperature", convert_temp)
        text = home.check_temp_and_perform_action(convert_temp)
        if(text=="Moisturizers"):
            Mos = Moisturizers(self.driver)
            Mos.product_click("Almond")
            time.sleep(2)
            Mos.product_click("Aloe")

        else:
            Sun = Sunscreen(self.driver)
            Sun.product_click_Sunscren("SPF-50")
            time.sleep(2)
            Sun.product_click_Sunscren("SPF-30")

        Tran = Transaction(driver)
        Mos = Moisturizers(driver)
        confirm = confirmation(driver)
        Mos.click_on_cart()
        Tran.payment()
        time.sleep(5)
        confirm.check_confirmation_msg()

































