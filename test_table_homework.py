import unittest
from selenium import webdriver

class TestTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/table-search-filter-demo.html')

    def test_user_enter_text(self):
        enter_text = self.driver.find_element_by_xpath('//input[@id="task-table-filter"]')
        enter_text.send_keys('bug fixing')

        filter_table = self.driver.find_element_by_xpath('//table[@id="task-table"]')
        assert filter_table.is_displayed()

    def test_correct_quantity_row(self):
        all_table = self.driver.find_elements_by_xpath('//table[@id="task-table"]//tbody/tr')
        assert len(all_table) == 7

    def test_incorrect_text(self):
        enter_incorrect_text = self.driver.find_element_by_xpath('//input[@id="task-table-filter"]')
        enter_incorrect_text.send_keys('it step')

        result = self.driver.find_element_by_xpath('//tbody/tr/td[contains(text(), "No results found")]')
        assert result.text == 'No results found'











