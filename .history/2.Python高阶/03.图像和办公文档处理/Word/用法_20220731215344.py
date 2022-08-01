import docx

doc = docx.Document('./File/test.docx')
print(len(doc.paragraphs))
