from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pytest
import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Testfile():
    @pytest.fixture()
    def test_setup(self):
        global driver      #Executes the chromedriver executable file from local directory.
        global driver      #To run this set up, you may need to create your own local directory#
        driver = webdriver.Chrome(executable_path="C:/Users/Cyril Obinna/PycharmProjects/Test Automation/chromedriver_"
                                                  "win32/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()

    #Navigates to landig page by launching the Url#
    def test_login(self, test_setup):
        driver.get("https://www.aoe.com")
        time.sleep(1)

    #Accepts cookies#
    def test_accept_cookie(self):
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(1)

    #Changes browser language#
    def test_switch_lang(self):
        driver.find_element_by_xpath("//*[@class='language ']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='language ']").click()
        time.sleep(1)

    #Displays main functions on the landing page by clicking on them#
    def test_display_header(self):
        driver.find_element_by_link_text("Agile").click()
        time.sleep(1)
        driver.find_element_by_link_text("Open Source").click()
        time.sleep(1)
        driver.find_element_by_link_text("Digitalization").click()
        time.sleep(1)
        driver.find_element_by_link_text("Enterprise").click()
        time.sleep(1)
        driver.find_element_by_link_text("Knowledge Base").click()
        time.sleep(1)

    #Hovers accross functions to display sub functions without clicking#
    def test_hover(self):
        element = driver.find_element_by_link_text("Solutions")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Products")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Clients")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Company")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Blog")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Careers")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_link_text("Contact")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element = driver.find_element_by_xpath("//i[@class='icon-search']")
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(1)

    def test_click(self):
        driver.find_element_by_xpath("//*[@data-qa='header-navigation-item-solutions']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@data-qa='header-navigation-item-products']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@data-qa='header-navigation-item-clients']").click()
        time.sleep(1)

    #Cloxks and swipes accross the function called client#
    def test_swipe_client(self):
        driver.find_element_by_xpath("//div[@class='swiper-button-next']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='swiper-button-next']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='swiper-button-next']").click()
        time.sleep(1)

    def test_continue_click(self):
        driver.find_element_by_xpath("//*[@data-qa='header-navigation-item-company']").click()
        time.sleep(1)
        driver.find_element_by_xpath(oe"//*[@data-qa='header-navigation-item-career']").click()
        time.sleep(1)

    #Displays the contact page, scrolls to the end of page and back to top of page#
    def test_contact(self):
        driver.find_element_by_xpath("//*[@data-qa='header-navigation-item-contact']").click()
        time.sleep(2)
        page = driver.find_element_by_tag_name("html")
        page.send_keys(Keys.END)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,400)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,50)")
        time.sleep(1)

    #Displays blogs by clicking and sending search keyword 'blog'#
    def test_search(self):
        driver.find_element_by_xpath("//i[@class='icon-search']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@ng-change='search.doSearch(search.searchTerm)']").send_keys("blog")
        time.sleep(1)

    #Selects a blog and displays it#
    def test_select_blog(self):
        driver.find_element_by_xpath("//*[@alt='Publishing Open Source extensions with minimal effort in 4 steps']").click()
        time.sleep(1)

    #Scrolls slowly accross page by pixels#
    def test_scroll_blog(self):
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,900)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1900)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,2200)")
        time.sleep(1)
        page = driver.find_element_by_tag_name("html")
        page.send_keys(Keys.END)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,50)")
        time.sleep(1)

    #Refreshes page#
    def test_refresh(self):
        driver.refresh()
        time.sleep(2)

    #Closes page#
    def test_Teardown(self):
        driver.close()
        driver.quit()
        print("Test completed")

        # To run on terminal, pytest -v, or pytest#

