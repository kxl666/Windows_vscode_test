import openpyxl

# 使用openpyxl模块创建新的空Excel文件
wb = openpyxl.Workbook()
# 获取活动的工作表
sheet = wb.active
# 修改工作表名称
sheet.title = 'Now Sheet'
