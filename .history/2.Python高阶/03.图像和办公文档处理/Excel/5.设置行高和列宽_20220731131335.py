import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.column_dimensions['A'].width = 30
sheet.column_dimensions['B'].width = 30
sheet.row_dimensions