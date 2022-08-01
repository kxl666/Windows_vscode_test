import openpyxl

# 使用openpyxl模块打开Excel文件
wb = openpyxl.load_workbook(r'./example.xlsx')

# 1.获取工作表
# 获取工作簿中的所有工作表
print(wb.get_sheet_names())
# 获取工作簿中的第一个工作表
sheet = wb.get_sheet_by_name('Sheet1')
# 修改工作表名称
sheet.title = 'New Sheet'
print(wb.get_sheet_names())
# 获取活动表的名称
print(wb.get_active_sheet().title)
