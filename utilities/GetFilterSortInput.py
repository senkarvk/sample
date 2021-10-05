from utilities import xlCommon
class GetFilterSortInput:
    def __init__(self,filename,sheetname):
        self.all_data_input=[]
        self.filename=filename
        self.sheetname=sheetname
        self.valid_column_vals = ['Name','Number of cases','Impact score','Complexity']
    def getAllRowsData(self):
        row_count=xlCommon.getRowCount(self.filename,self.sheetname)
        print('number of data rows are:',row_count-1)
        for row in range(2,row_count+1):
            tmp=[]
            valid_row_flag=0
            filter_cell_val=str(xlCommon.getCellValue(self.filename, self.sheetname, row, 1))
            print('filter_cell_val',filter_cell_val,type(filter_cell_val),len(filter_cell_val))
            sort_cell_val=str(xlCommon.getCellValue(self.filename, self.sheetname, row, 2))
            print('sort_cell_val', sort_cell_val,type(sort_cell_val),len(sort_cell_val))
            #checking for valid input values
            valid_filter_input=False
            valid_sort_input=False
            for i in self.valid_column_vals:
                if sort_cell_val==i.lower():
                    valid_sort_input = True
                    sort_cell_val=i
                    print('sort_cell_val', sort_cell_val, type(sort_cell_val))
                    break

            if sort_cell_val in self.valid_column_vals:
                valid_sort_input=True
            elif sort_cell_val.isspace() or len(sort_cell_val)==0 :
                sort_cell_val=''
                valid_sort_input = True
            if filter_cell_val.isspace() or len(filter_cell_val)>=0:
                valid_filter_input=True
            print("valid_sort_input {} and valid_filter_input {}".format(valid_sort_input,valid_filter_input))
            if valid_sort_input and valid_filter_input:
                tmp.append(filter_cell_val)
                tmp.append(sort_cell_val)
            self.all_data_input.append(tmp)
        print(self.all_data_input)
        return self.all_data_input
