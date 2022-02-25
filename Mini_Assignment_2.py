import pytest
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def test_button():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='BUTTON CLICKS']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID, 'button1').click()
    time.sleep(5)
    button1 = driver.find_element(By.XPATH, "//h4[text()='Congratulations!']").text
    print(button1)
    assert button1 == 'Congratulations!'
    driver.find_element(By.XPATH, "//button[text()='Close']").click()
    driver.quit()


def test_dropdowmn():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']").click()
    driver.switch_to.window(driver.window_handles[1])
    select = Select(driver.find_element(By.XPATH, "//select[@id='dropdowm-menu-1']"))
    select.select_by_index('2')
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@value='option-1']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@value='green']").click()
    driver.find_element(By.XPATH, "//input[@value='lettuce']").click()
    select1 = Select(driver.find_element(By.ID, 'fruit-selects'))
    select1.select_by_index('2')
    driver.quit()


def test_textfield():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='AUTOCOMPLETE TEXTFIELD']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID, 'myInput').send_keys("Test")
    time.sleep(4)
    driver.find_element(By.ID, 'submit-button').click()
    driver.quit()


def test_scrolldown():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='SCROLLING AROUND']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("window.scrollTo(0, 778)")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, 50)")
    driver.quit()


def test_to_do_list():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='TO DO LIST']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys("Test1")
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="container"]/ul/li[4]').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="container"]/ul/li[4]/span/i').click()
    time.sleep(4)
    driver.quit()


def test_fileupload():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='FILE UPLOAD']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID, 'myFile').send_keys("/Users/sukjain/Desktop/Test.png")
    time.sleep(4)
    driver.find_element(By.ID, 'submit-button').click()
    time.sleep(4)
    driver.quit()


def test_Actions():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='ACTIONS']").click()
    driver.switch_to.window(driver.window_handles[1])
    actionChains = ActionChains(driver)
    source_element = driver.find_element(By.ID, 'draggable')
    dest_element = driver.find_element(By.ID, 'droppable')
    actionChains.drag_and_drop(source_element, dest_element).perform()
    color_chng = driver.find_element(By.ID, 'double-click')
    actionChains.double_click(color_chng).perform()
    first_hover = driver.find_element(By.XPATH, "//button[text()= 'Hover Over Me First!']")
    actionChains.move_to_element(first_hover).perform()
    second_hover = driver.find_element(By.XPATH, "//button[text()= 'Hover Over Me Second!']")
    actionChains.move_to_element(second_hover).perform()
    third_hover = driver.find_element(By.XPATH, "//button[text()= 'Hover Over Me Third!']")
    actionChains.move_to_element(third_hover).perform()

    click_box1 = driver.find_element(By.ID, 'click-box')
    actionChains.click_and_hold(on_element=click_box1).perform()

    double_click = click_box1.text
    print(double_click)
    assert double_click == 'Well done! keep holding that click now.....'
    driver.quit()


def test_datepicker():
    driver = webdriver.Chrome(executable_path="/Users/sukjain/PycharmProjects/naveen_automation/venv/bin/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.find_element(By.XPATH, "//h1[text()='DATEPICKER']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID, 'datepicker').click()
    # driver.find_element(By.XPATH, "// td[text() = '23']").click()
    all_date = driver.find_elements(By.XPATH, "//table[@class=' table-condensed']//td")
    for date in all_date:
        d = date.text
        print(d)
        if d == '25':
            date.click()
            time.sleep(10)
            break
            assert driver.find_element(By.XPATH, "//h1[text()='DATEPICKER']").text == "25-12-2021"
            driver.quit
