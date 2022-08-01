import openpyxl
from openpyxl.styles import Font, styleable

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Fonts'
sheet['A1'].value = 'Hello'
sheet['A1'].font = Font(size=20, bold=True, italic=True, color='FF0000')
sheet['A2'].value = 'World'
