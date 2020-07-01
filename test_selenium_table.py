import unittest
from selenium import webdriver

class TestTable(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/table-pagination-demo.html')

    def test_table_total_rows(self):
        table_rows = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr')
        assert len(table_rows) == 13

    def test_total_rows_cells(self):
        all_table_cells = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr/td')
        assert len(all_table_cells) == 91

    def test_cell_name(self):
        all_cells = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr[2]/td')
        assert all_cells[4].text == 'Table cell'
        cell_names = []
        for names in all_cells:
            cell_names.append(names.text)

        assert cell_names[3] == 'Table cell'

    def test_correct_text_in_list(self):
        table_heading = self.driver.find_elements_by_xpath('//thead[@class="btn-primary"]')
        list = []
        for a in table_heading:
            list.append(a.text)
        assert list[6] == 'Table heading 5'

    def test_correct_text(self):
        table_heading = self.driver.find_element_by_xpath('//thead/tr/th[6]')
        assert table_heading.text == 'Table heading 5'

    def test_correct_header(self):
        table_header = self.driver.find_elements_by_xpath('//thead[@class="btn-primary"]/tr/th')
        assert len(table_header) == 7






