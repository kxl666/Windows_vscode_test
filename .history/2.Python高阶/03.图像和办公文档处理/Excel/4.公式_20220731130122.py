import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '公式'
sheet['A1'].value = 100
sheet['A2'].value = 200
sheet['A3'].value = 300
