import PyPDF2

pdfFileObj = open('./File/Python数据科学手册.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# 1.从PDF提取文本
print(pdfReader.numPages)  # 输出PDF文件的页数
pageObj = pdfReader.getPage(10)  # 获取第一页的内容
print(pageObj.extractText())  # 输出第一页的内容

# 2.解密PDF文件
print(pdfReader.isEncrypted)  # 检查PDF文件是否加密,如果是True则表示加密
# pdfReader.decrypt('rosebud')  # 解密PDF文件

# 3.创建新的PDF文件
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)
