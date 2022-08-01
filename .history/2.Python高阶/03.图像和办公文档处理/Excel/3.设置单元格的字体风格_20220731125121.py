from openpyxl.styles import Font, Style
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Fonts'
sheet['A1'].value = 'Hello'
sheet['A1'].font = Font(bold=True, size=24, color='FF0000', italic=)