import HtmlTestRunner
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls): #Test function#
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Cyril Obinna/PycharmProjects/Test Automation/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self): #Test function#
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_xpath("//*[@class='button']").click()
        self.driver.find_element_by_xpath("//*[@class='panelTrigger']").click()
        self.driver.find_element_by_id("aboutDisplayLink").click()
        self.driver.find_element_by_xpath("//*[@class='close']").click()
        self.driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Dashboard").click()
        time.sleep(1)
        self.driver.find_element_by_id("welcome").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(1)

    def test_logout(self): #Test function#
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()

#To Run on Terminal = python -m login#

