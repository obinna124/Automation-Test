from selenium import webdriver
import time
import pytest
import HtmlTestRunner
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Testfile():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Cyril Obinna/PycharmProjects/Test Automation/chromedriver_win32/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()


    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_xpath("//*[@class='button']").click()

    def test_landingPageHover(self):
        element = driver.find_element_by_link_text("Admin")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("PIM")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Leave")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Recruitment")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Performance")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Maintenance")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)

    def test_landingPageClick(self):
        driver.find_element_by_xpath("//*[@class='firstLevelMenu']").click()
        time.sleep(1)

    def test_Sub_Honer(self):
        element = driver.find_element_by_link_text("User Management")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        driver.find_element_by_id("ohrmList_chkSelectAll").click()
        time.sleep(1)
        driver.find_element_by_id("ohrmList_chkSelectAll").click()
        time.sleep(1)
        element = driver.find_element_by_link_text("Job")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Qualifications")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Configuration")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)

    def test_click_On(self):
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(1)
        driver.find_element_by_id("menu_leave_viewLeaveModule").click()
        time.sleep(1)
        driver.find_element_by_id("menu_time_viewTimeModule").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='panelTrigger']").click()
        driver.find_element_by_id("aboutDisplayLink").click()
        driver.find_element_by_xpath("//*[@class='close']").click()
        driver.find_element_by_link_text("Dashboard").click()
        time.sleep(1)

    def test_logout(self):
        driver.find_element_by_id("welcome").click()
        time.sleep(1)
        driver.find_element_by_link_text("Logout").click()

    def test_close(self):
        driver.close()
        driver.quit()
        print("Test Completed")

        #To run on terminal, pytest -v, or pytest#

