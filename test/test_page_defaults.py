import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from page.TablePage import TablePage
from utilities import xlCommon
from pathlib import Path
import allure
class Test_default:
    testDataFolder = Path("./test_data")
    test_data_file = testDataFolder / "TableData.xlsx"
    baseURL = ReadConfig.getApplicationURL()
    @allure.title("Login with valid data test")
    def test_default_sort_option(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.table_obj=TablePage(self.driver)
        default_act_sort_option_set = self.table_obj.getSortOtionSet()
        default_exp_sort_option_set = xlCommon.getCellValue(self.test_data_file, 'testdata', 2, 2)
        if default_act_sort_option_set == default_exp_sort_option_set:
            assert True
            self.driver.quit()
        else:
            self.driver.quit()
            print(f'actual {default_act_sort_option_set} expected {default_exp_sort_option_set}')
            assert False
    def test_default_filter_val(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.table_obj=TablePage(self.driver)
        default_act_filter_val_set = self.table_obj.getFilterValue()
        default_exp_filter_val_set = xlCommon.getCellValue(self.test_data_file, 'testdata', 2, 1)
        if default_act_filter_val_set == default_exp_filter_val_set:
            assert True
            self.driver.quit()
        else:
            self.driver.quit()
            print(f'actual :{default_act_filter_val_set}: expected :{default_exp_filter_val_set}:')
            assert False