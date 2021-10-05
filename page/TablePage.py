from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
class TablePage:
    app_id='app'
    filter_class_name='filtering'
    filter_text_tag_name='label'
    filter_text_area_id='filter-input'
    sort_class_name='sorting'
    sort_text_tag_name='label'
    sort_select_id='sort-select'
    sort_select_options_tag_name='option'
    table_class_name='table'
    table_header_class_name='table-header'
    table_content_class_name='table-content'
    table_rows_class_name='table-row'
    table_columns_class_name='table-data'
    table_rows_tag_name='div'
    default_sort_option='Name'
    def __init__(self,driver):
        self.driver=driver
    def setFilter(self,filter_data):
        self.driver.find_element_by_id(self.filter_text_area_id).send_keys(filter_data)
    def getFilterValue(self):
        return self.driver.find_element_by_id(self.filter_text_area_id).get_attribute('value')
    def getSortOptions(self):
        sort_select = self.driver.find_element_by_id(self.sort_select_id)
        sort_select_options = sort_select.find_elements_by_tag_name(self.sort_select_options_tag_name)
        self.column_names = []
        for optn in sort_select_options:
            self.column_names.append(optn.text)
        return self.column_names
    def getSortOtionSet(self):
        sort_select = self.driver.find_element_by_id(self.sort_select_id)
        select_op=Select(sort_select)
        select_op.first_selected_option.text
        return select_op.first_selected_option.text
    def setSortOptions(self,sort_option):
        sort_select = self.driver.find_element_by_id(self.sort_select_id)
        selectSortBy=Select(sort_select)
        selectSortBy.select_by_visible_text(sort_option)
    def getTableRows(self):
        table_content=self.driver.find_element_by_class_name(self.table_content_class_name)
        table_rows = table_content.find_elements_by_class_name(self.table_rows_class_name)
        num_rows = len(table_rows)
        self.rows_list = []
        if num_rows==0:
            return self.rows_list
        num_columns = len(table_rows[0].find_elements_by_class_name(self.table_columns_class_name))
        for i in table_rows:
            tmp = []
            for j in i.find_elements_by_tag_name(self.table_rows_tag_name):
                tmp.append(j.text)
            self.rows_list.append(tmp)
        return self.rows_list
    def setToDefaults(self):
        self.driver.find_element_by_id(self.filter_text_area_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_id(self.filter_text_area_id).send_keys(Keys.DELETE)
        sort_select = self.driver.find_element_by_id(self.sort_select_id)
        selectSortBy = Select(sort_select)
        selectSortBy.select_by_visible_text(self.default_sort_option)



