import unittest
from selenium import webdriver


class TestTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/table-search-filter-demo.html')

    def test_quantity_rows(self):
        rows = self.driver.find_element_by_xpath('//input[@id="task-table-filter"]')
        rows.send_keys('failed qa')

        show = self.driver.find_elements_by_xpath('//tbody/tr[@style="display: table-row;"]')
        list = []
        for i in show:
            list.append(i)
        assert len(show) == 2




