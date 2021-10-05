import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from page.TablePage import TablePage
from utilities import xlCommon
from pathlib import Path
from utilities import common_python_functions
from utilities import GetFilterSortInput
import allure
class Test_Filter_Sort:
    testDataFolder = Path("./test_data")
    test_data_file = testDataFolder / "TableData.xlsx"
    baseURL = ReadConfig.getApplicationURL()
    @allure.title("Test Sort and Filter with test data")
    def test_sort_filter_table(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.table_obj=TablePage(self.driver)
        test_data_fromxl=GetFilterSortInput.GetFilterSortInput(self.test_data_file, 'testdata')
        self.rows_test_data=test_data_fromxl.getAllRowsData()
        self.rows_count=len(self.rows_test_data)
        print("number of rows in testdata excel are :",self.rows_count)
        fn_status=[]
        for rw in self.rows_test_data:
            self.table_obj.setToDefaults()
            print("********Executing for case",rw,"********")
            # read filter and sort values from excel testdata sheet
            self.filter_set_val = rw[0]
            self.sort_set_val = rw[1]
            # get the initial table rows from application page
            initial_rows = self.table_obj.getTableRows()
            print('initial state of table rows are :',initial_rows)
            # filter and sort the rows using python logic-for EXPECTED
            column_headers=self.table_obj.getSortOptions()
            if len(self.sort_set_val)==0 and len(self.filter_set_val)!=0:
                # filter values in the application
                self.table_obj.setFilter(self.filter_set_val)
            elif len(self.sort_set_val)!=0 and len(self.filter_set_val)==0:
                # sort values in the application
                self.table_obj.setSortOptions(self.sort_set_val)
            elif len(self.sort_set_val)!=0 and len(self.filter_set_val)!=0:
                # set the filter and sort values in the application
                self.table_obj.setFilter(self.filter_set_val)
                self.table_obj.setSortOptions(self.sort_set_val)
            exp_sort_filter_rows = common_python_functions.filter_sort(initial_rows, self.filter_set_val,
                                                                       self.sort_set_val, column_headers)
            print('expected rows are :',exp_sort_filter_rows)
            #get the table values from application page - for ACTUAL
            act_sort_filter_rows_beforeConvert=self.table_obj.getTableRows()
            act_sort_filter_rows=common_python_functions.convert_data(act_sort_filter_rows_beforeConvert,
                                                                      column_headers)
            print('after filter, and sort, state of table rows are :', act_sort_filter_rows)
            #compare EXPECTED to ACTUAL
            if act_sort_filter_rows == exp_sort_filter_rows:
                fn_status.append("pass")
            else:
                fn_status.append("fail")
        print(fn_status)
        if "fail" not in fn_status:
            print('Test case passed')
            self.driver.close()
            assert True
        else:
            print('Test case failed')
            self.driver.close()
            assert False
        print('Test case completed')