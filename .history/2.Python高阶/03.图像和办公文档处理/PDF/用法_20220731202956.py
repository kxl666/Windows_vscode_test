import PyPDF2

pdfFileObj = open('./File/员工保密协议.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)  # 输出PDF文件的页数
pageObj = pdfReader.getPage(0)  # 获取第一页的内容
print(pageObj.extractText())  # 输出第一页的内容
