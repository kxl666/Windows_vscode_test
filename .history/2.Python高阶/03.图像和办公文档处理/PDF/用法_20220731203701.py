import PyPDF2

pdfFileObj = open('./File/Python数据科学手册.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)  # 输出PDF文件的页数
pageObj = pdfReader.getPage(10)  # 获取第一页的内容
print(pageObj.extractText())  # 输出第一页的内容
