import PyPDF2

pdfFileObj = open('./File/员工保密协议.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
