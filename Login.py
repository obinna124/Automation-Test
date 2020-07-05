import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import unittest

#Implement Unittest framewoerk from python Library#
class LoginTest(unittest.TestCase):
    @classmethod

    def setUpClass(cls): #Launches chrome executable from local directory#
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Cyril Obinna/PycharmProjects/Test Automation/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    #Launches the Url#
    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")

    #Sends login credential both for username and password#
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='button']").click()
        time.sleep(1)

    #Clicks on selected functions to display content#
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        time.sleep(1)
        self.driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Dashboard").click()
        time.sleep(1)
        self.driver.find_element_by_id("welcome").click()
        time.sleep(1)
        self.driver.find_element_by_id("aboutDisplayLink").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='close']").click()

    #Clicks on the logout button to log user out#
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(1)
    #Initiates tear down to close browser#
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()

#To Run on Terminal = python Login.py#

