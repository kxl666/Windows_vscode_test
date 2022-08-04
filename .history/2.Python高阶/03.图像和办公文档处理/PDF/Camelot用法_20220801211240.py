from msilib.schema import File

import camelot

# 提取PDF文档中的表格
tables = camelot.read_pdf('./File/combine.pdf')
print(tables)
tables.export("./File/extracted.csv", f="csv", compress=True)  # 导出表格
# 提取Excel文档中的表格
# tables = camelot.read_excel("tables.xlsx")
# print(tables)
# tables.export("extracted.csv", f="csv", compress=True) # 导出表格
