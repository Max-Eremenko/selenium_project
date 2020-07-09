import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html')

    def test_get_random_user_img(self):
        button_get_new_user = self.driver.find_element_by_xpath('//button[@type="button"][@class="btn btn-default"]')
        button_get_new_user.click()

        wait_for_image = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="loading"]/img[@src]')))

        img = self.driver.find_element_by_xpath('//div[@id="loading"]/img[@src]')
        assert img.is_displayed()

    def test_get_first_name(self):
        button_get_new_user = self.driver.find_element_by_xpath('//button[@type="button"][@class="btn btn-default"]')
        button_get_new_user.click()

        first_name = self.driver.find_element_by_xpath('//*[text()[contains(.,"First")]]')
        assert first_name.is_displayed()

    def test_get_last_name(self):
        button_get_new_user = self.driver.find_element_by_xpath('//button[@type="button"][@class="btn btn-default"]')
        button_get_new_user.click()

        last_name = self.driver.find_element_by_xpath('//*[text()[contains(.,"Last")]]')
        assert last_name.is_displayed()








