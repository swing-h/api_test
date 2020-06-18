import xlrd

def excel_to_list(data_file, sheet):
    #新建空列表，乘装所有的数据
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    #获取标题行数据
    header = sh.row_values(0)

    #跳过标题行，从第二行开始取数据
    for i in range(1, sh.nrows):
        #将标题行和每行数据组装成字典
        d = dict(zip(header, sh.row_values(i)))
        data_list.append(d)
    #列表嵌套字典格式，每个元素是一个字典
    return data_list

def get_test_data(data_list, case_name):
    for case_data in data_list:
        #如果字典数据中case_name与参数一致
        if case_name == case_data['case_name']:
            return case_data
        #如果查询不到会返回None

if __name__ == "__main__":
    # 读取excel，TestUserLogin工作簿的所有数据
    data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")
    # 查找用例'test_user_login_normal'的数据
    case_data = get_test_data(data_list, 'test_user_login_normal')
    print(case_data)