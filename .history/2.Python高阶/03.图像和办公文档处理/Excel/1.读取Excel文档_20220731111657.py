import openpyxl

# 使用openpyxl模块打开Excel文件
wb = openpyxl.load_workbook(r'./example.xlsx')

# 获取工作表
# 获取工作簿中的所有工作表
print(wb.get_sheet_names())
