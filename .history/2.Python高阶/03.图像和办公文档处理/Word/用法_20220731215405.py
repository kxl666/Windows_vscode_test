import docx

doc = docx.Document('./File/test.docx')
# 返回文档的
print(len(doc.paragraphs))
