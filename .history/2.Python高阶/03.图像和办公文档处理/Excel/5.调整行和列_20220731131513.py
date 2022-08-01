import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'].value = '行高'
sheet['B1'].value = '列宽'
sheet.column_dimensions['A'].width = 50
sheet.column_dimensions['B'].width = 70
sheet.row_dimensions[1].height = 30

wb.save(r'./File/example02.xlsx')
