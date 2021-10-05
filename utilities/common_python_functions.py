def filter_list(dt,filter_text,column_subset):
    #added only below two as filtering works for only these 2 columns
    name_index=column_subset.index('Name')
    complexity_index=column_subset.index('Complexity')
    dt_filtered=[]
    print('filter_text = ',filter_text,type(filter_text))
    for i in dt:
        if filter_text in i[name_index].lower() or filter_text in i[complexity_index]:
            dt_filtered.append(i)
    return dt_filtered
def convert_names(nms):
    return nms.lower()
def convert_cases(cases):
    mul={'K':1000,'M':1000000,'B':1000000000}
    if 'k' in cases or 'K' in cases:
        return (float(cases[0:-1])*mul['K'])
    elif 'm' in cases or 'M' in cases:
        return (float(cases[0:-1])*mul['M'])
    elif 'b' in cases or 'B' in cases:
        return (float(cases[0:-1])*mul['B'])
    else:
        return float(cases)
def convert_complexity(compl):
    comp={'low':0,'medium':1,'high':2}
    return comp[compl]
def convert_data(lst,column_subset):
    name_index = column_subset.index('Name')
    cases_index=column_subset.index('Number of cases')
    score_index=column_subset.index('Impact score')
    complexity_index=column_subset.index('Complexity')
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j == name_index:
                lst[i][j] = convert_names(lst[i][j])
            elif j == cases_index:
                lst[i][j]=convert_cases(lst[i][j])
            elif j==score_index:
                lst[i][j]=float(lst[i][j])
            elif j==complexity_index:
                lst[i][j]=convert_complexity(lst[i][j])
    return lst
#function to sort by column
def sort_by_col(dt_copy,sort_by_column,column_subset):
    column_index=column_subset.index(sort_by_column)
    dt_copy.sort(key = lambda x: x[column_index])
    return dt_copy
#function to filter and sort
def filter_sort(ar_tmp,filter_text,sort_by_column,column_subset):
    #only filtering
    print("********in filter sort***********")
    if len(sort_by_column)==0 and len(filter_text)!=0:
        flr = filter_list(ar_tmp, filter_text, column_subset)
        dt_after_filter_convert=convert_data(flr,column_subset)
        return dt_after_filter_convert
    #only sorting
    elif len(filter_text)==0 and len(sort_by_column)!=0:
        dt_after_convert=convert_data(ar_tmp,column_subset)
        dt_after_convert_sort=sort_by_col(dt_after_convert,sort_by_column,column_subset)
        return dt_after_convert_sort
    elif len(filter_text)!=0 and len(sort_by_column)!=0:
        flr = filter_list(ar_tmp, filter_text, column_subset)
        dt_after_filter_convert = convert_data(flr, column_subset)
        dt_after_filter_convert_sort = sort_by_col(dt_after_filter_convert, sort_by_column, column_subset)
        return dt_after_filter_convert_sort
