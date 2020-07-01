from selenium import webdriver
import time
import pytest
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Testfile():
    @pytest.fixture()
    def test_setup(self): #Test function#
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Cyril Obinna/PycharmProjects/Test Automation/chromedriver_win32/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()


    def test_login(self,test_setup): #Test function#
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_xpath("//*[@class='button']").click()
        driver.find_element_by_xpath("//*[@class='panelTrigger']").click()
        driver.find_element_by_id("aboutDisplayLink").click()
        driver.find_element_by_xpath("//*[@class='close']").click()
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(1)
        driver.find_element_by_link_text("Dashboard").click()
        time.sleep(1)
        driver.find_element_by_id("welcome").click()
        time.sleep(1)
    def test_logout(self): #Test function#
        driver.find_element_by_link_text("Logout").click()

    def test_close(self): #Test function#
        driver.close()
        driver.quit()
        print("Test Completed")

#To run on terminal, pytest -v, or pytest#

