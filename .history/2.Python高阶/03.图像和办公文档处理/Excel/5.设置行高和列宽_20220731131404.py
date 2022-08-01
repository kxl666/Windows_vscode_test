import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.column_dimensions['A'].width = 50
sheet.column_dimensions['B'].width = 70
sheet.row_dimensions[1].height = 30

wb.save(r'./File/example02.xlsx')
