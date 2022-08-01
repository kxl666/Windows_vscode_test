import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '公式'
sheet['A1'].value = 'Hello'