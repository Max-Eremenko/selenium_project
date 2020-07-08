import unittest
from selenium import webdriver


class TestSelectDays(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')

    # def test_select_days(self):
    #     click_on_the_please_select = self.driver.find_element_by_xpath('//select[@id="select-demo"]')
    #     click_on_the_please_select.click()
    #
    #     select_day = self.driver.find_elements_by_xpath('//option[@value][contains(text(), "day")]')
    #     list = []
    #     for i in select_day:
    #         list.append(i)
    #
    #     Sunday = list[0].click()
    #     Monday = list[1].click()
    #     Tuesday = list[2].click()
    #     Wednesday = list[3].click()
    #     Thursday = list[4].click()
    #     Friday = list[5].click()
    #     Saturday = list[6].click()
    #
    #     get_the_result = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
    #     assert get_the_result.is_displayed()
    #
    # def test_select_one_day(self):
    #     click_on_the_please_select = self.driver.find_element_by_xpath('//select[@id="select-demo"]')
    #     click_on_the_please_select.click()
    #
    #     select_day = self.driver.find_element_by_xpath('//select[@id="select-demo"]/option[@value="Saturday"]')
    #     select_day.click()
    #
    #     get_the_result = self.driver.find_element_by_xpath('//p[@class="selected-value"][contains(text(), "Saturday")]')
    #     assert get_the_result.is_displayed()
    #
    # def test_select_all_cities_first_button(self):
    #     list_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
    #     list = []
    #     for b in list_cities:
    #         list.append(b)
    #
    #     California = list[0].click()
    #     Florida = list[1].click()
    #     New_Jersey = list[2].click()
    #     New_York = list[3].click()
    #     Ohio = list[4].click()
    #     Texas = list[5].click()
    #     Pennsylvania = list[6].click()
    #     Washington = list[7].click()
    #
    #     button_first_selected = self.driver.find_element_by_xpath('//button[@id="printMe"]')
    #     button_first_selected.click()
    #
    #     result_option = self.driver.find_element_by_xpath('//p[@class="getall-selected"]')
    #     assert result_option.is_displayed()
    #
    # def test_select_all_cities_get_all_button(self):
    #     list_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
    #     list = []
    #     for b in list_cities:
    #         list.append(b)
    #
    #     California = list[0].click()
    #     Florida = list[1].click()
    #     New_Jersey = list[2].click()
    #     New_York = list[3].click()
    #     Ohio = list[4].click()
    #     Texas = list[5].click()
    #     Pennsylvania = list[6].click()
    #     Washington = list[7].click()
    #
    #     button_get_all_selected = self.driver.find_element_by_xpath('//button[@value="Print All"]')
    #     button_get_all_selected.click()
    #
    #     result_option = self.driver.find_element_by_xpath('//p[@class="getall-selected"]')
    #     assert result_option.is_displayed()
    #
    # def test_select_one_city_first_button(self):
    #     select_the_city = self.driver.find_element_by_xpath('//select[@id="multi-select"]/option[text()="Florida"]')
    #     select_the_city.click()
    #
    #     click_on_the_first_selected = self.driver.find_element_by_xpath('//button[@id="printMe"]')
    #     click_on_the_first_selected.click()
    #
    #     result_option = self.driver.find_element_by_xpath('//p[@class="getall-selected"][contains(text(), "Florida")]')
    #     assert result_option.is_displayed()
    #
    # def test_select_one_city_get_all_button(self):
    #     select_the_city = self.driver.find_element_by_xpath('//select[@id="multi-select"]/option[text()="Texas"]')
    #     select_the_city.click()
    #
    #     click_on_the_get_all_selected = self.driver.find_element_by_xpath('//button[@id="printAll"]')
    #     click_on_the_get_all_selected.click()
    #
    #     result_option = self.driver.find_element_by_xpath('//p[@class="getall-selected"][contains(text(), "Texas")]')
    #     assert result_option.is_displayed()
    #
    # def test_select_nothing_first_button(self):
    #     click_on_the_first_selected = self.driver.find_element_by_xpath('//button[@id="printMe"]')
    #     click_on_the_first_selected.click()
    #
    #     result = self.driver.find_element_by_xpath('//p[@class="getall-selected"][contains(text(), "undefined")]')
    #     assert result.is_displayed()
    #
    # def test_select_nothing_get_all_button(self):
    #     click_on_the_get_all = self.driver.find_element_by_xpath('//button[@id="printAll"]')
    #     click_on_the_get_all.click()
    #
    #     result = self.driver.find_element_by_xpath('//p[@class="getall-selected"][contains(text(), "")]')
    #     assert result.is_displayed()

    def test_click_on_select_days_many_times(self):
        click_on_button_two_times = self.driver.find_element_by_xpath('//select[@id="select-demo"]')
        assert click_on_button_two_times.click()
