from openpyxl.styles import Alignment, Font

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Fonts'
sheet['A1'].value = 'Hello'
sheet['A1'].font = openpyxl.styles.Font(size=20,
                                        bold=True,
                                        italic=True,
                                        color='FF0000')
sheet['A2'].value = 'World'
