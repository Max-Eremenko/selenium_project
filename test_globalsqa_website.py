import unittest
from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException


class TestingFeatures(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('http://www.globalsqa.com/demo-site/')

    # def test_alert_box_simple(self):
    #     click_on_alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
    #     click_on_alertbox.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-labelledby="tab_item-0"]//button')))
    #
    #     click_on_try_it = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-0"]//button')
    #     click_on_try_it.click()
    #
    #     result = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-0"]//button')
    #     assert result.is_displayed()
    #
    # def test_alertbox_confirmation_box(self):
    #     click_on_alertbox = self.driver.find_element_by_xpath(
    #         '//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
    #     click_on_alertbox.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//li[@id="Confirmation Box"]')))
    #
    #     go_to_confirmation_box = self.driver.find_element_by_xpath('//li[@id="Confirmation Box"]')
    #     go_to_confirmation_box.click()
    #
    #     click_on_try_it = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-1"]//button')
    #     click_on_try_it.click()
    #
    #     result = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-1"]//button')
    #     assert result.is_displayed()
    #
    # def test_prompt_box(self):
    #     click_on_alertbox = self.driver.find_element_by_xpath(
    #         '//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
    #     click_on_alertbox.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Prompt Box"]')))
    #
    #     go_to_prompt_box = self.driver.find_element_by_xpath('//li[@id="Prompt Box"]')
    #     go_to_prompt_box.click()
    #
    #     click_on_try_it = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-2"]//button')
    #     click_on_try_it.click()
    #
    #     result = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-2"]//button')
    #     assert result.is_displayed()
    #
    # def test_frames_open_new_tab(self):
    #     click_on_frames = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/frames-and-windows/"][text()="Frames"]')
    #     click_on_frames.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/a')))
    #
    #     click_on_click_here = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/a')
    #     click_on_click_here.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.new_window_is_opened)
    #
    #     result = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/a')
    #     assert result.is_displayed()
    #
    # def test_frames_open_new_window(self):
    #     click_on_frames = self.driver.find_element_by_xpath(
    #         '//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/frames-and-windows/"][text()="Frames"]')
    #     click_on_frames.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Open New Window"]')))
    #
    #     click_on_open_new_window = self.driver.find_element_by_xpath('//li[@id="Open New Window"]')
    #     click_on_open_new_window.click()
    #
    #     click_on_click_here = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/a')
    #     click_on_click_here.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.new_window_is_opened)
    #
    #     result = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/a')
    #     assert result.is_displayed()

    # def test_sorting_portlets(self):
    #     click_on_sorting = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/sorting/"]')
    #     click_on_sorting.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="portlet-header ui-sortable-handle ui-widget-header ui-corner-all"]/span[@class="ui-icon portlet-toggle ui-icon-minusthick"]')))
    #
    #     click_on_feeds = self.driver.find_element_by_xpath('//div[@class="portlet-header ui-sortable-handle ui-widget-header ui-corner-all"]/span[@class="ui-icon portlet-toggle ui-icon-minusthick"]')
    #     click_on_feeds.click()
    #
    #     result = self.driver.find_element_by_xpath('//span[@class="ui-icon portlet-toggle ui-icon-plusthick"]')
    #     assert result.is_displayed()

    def test_dialog_box_form(self):
        click_on_dialog_box = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/dialog-boxes/"]')
        click_on_dialog_box.click()

        # click_alert = Alert(driver=hh)
        # click_alert.send_keys('hi')
        # click_alert.accept()

        # wait_for = WebDriverWait(self.driver, 5).until(EC.((By.XPATH, '//div[@id="users-contain"]')))
        wait_for = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it)
     

        click_on_create_new_user = self.driver.find_element_by_xpath('//button[@id="create-user"][text()="Create new user"]')
        click_on_create_new_user.click()

        wait_for = WebDriverWait(self.driver, 5).until(EC.new_window_is_opened((By.XPATH, '//div[@id="dialog-form"]')))

        enter_name = self.driver.find_element_by_xpath('//input[@name="name"]')
        enter_name.clear()
        enter_name.send_keys('John Smith')

        enter_email = self.driver.find_element_by_xpath('//input[@name="email"]')
        enter_email.clear()
        enter_email.send_keys('jsmith1991@yahoo.com')

        enter_password = self.driver.find_element_by_xpath('//input[@name="password"]')
        enter_password.clear()
        enter_password.send_keys('lovemycity111')

        click_on_create_an_account = self.driver.find_element_by_xpath('//button[@type="button"][text()="Create an account"]')
        click_on_create_an_account.click()

        result_new_user = self.driver.find_element_by_xpath('//table[@id="users"]/tbody/tr[2]')
        assert result_new_user.is_displayed()

    # def test_message_box(self):
    #     click_on_dialog_box = self.driver.find_element_by_xpath(
    #         '//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/dialog-boxes/"]')
    #     click_on_dialog_box.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Message Box"]')))
    #
    #     go_to_message_box = self.driver.find_element_by_xpath('//li[@id="Message Box"]')
    #     go_to_message_box.click()
    #
    #     wait_for = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button"][text()="Ok"]')))
    #
    #     click_on_ok = self.driver.find_element_by_xpath('//button[@type="button"][text()="Ok"]')
    #     click_on_ok.click()
    #
    #     click_on_rutrum_convallis = self.driver.find_element_by_xpath('//p/a[@href="http://example.com"]')
    #     click_on_rutrum_convallis.click()
    #
    #     result = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]')
    #     assert result.is_displayed()



























