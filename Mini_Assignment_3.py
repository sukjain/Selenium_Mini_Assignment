
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(3)
driver.switch_to.alert.send_keys("ABC")
time.sleep(3)
driver.switch_to.alert.accept()
result= driver.find_element(By.XPATH, "//p[@id='result']").text
print(result)
if result=="You entered: ABC":
    print("pass")

print("Result is matching")

#driver.close()

