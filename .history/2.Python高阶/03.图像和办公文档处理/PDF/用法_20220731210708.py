import PyPDF2

pdfFileObj = open('./File/Python数据科学手册.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# 1.从PDF提取文本
print(pdfReader.numPages)  # 输出PDF文件的页数
pageObj = pdfReader.getPage(10)  # 获取第十页的内容
print(pageObj.extractText())  # 输出第一页的内容

# 2.解密PDF文件
print(pdfReader.isEncrypted)  # 检查PDF文件是否加密,如果是True则表示加密
# pdfReader.decrypt('rosebud')  # 解密PDF文件

# 3.创建新的PDF文件
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)  # 将第一页添加到新的PDF文件中

# 4.拷贝页面,将两个PDF文件合并成一个
pdf1File = open('./File/pdf01.pdf', 'rb')
pdf2File = open('./File/pdf02.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# 创建一个PDF文件写入对象
pdfWriter = PyPDF2.PdfFileWriter()
# 将两个PDF文件中的页面循环添加到新的PDF文件中
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

with open('./File/combine.pdf', 'wb') as pdfOutputFile:
    pdfWriter.write(pdfOutputFile)
pdf1File.close()
pdf2File.close()

#