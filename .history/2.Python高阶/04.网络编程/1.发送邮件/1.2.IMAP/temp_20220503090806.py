import imapclient

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
imapObj.login('2244951869@qq.com', 'eezkyozvtsgpdjad')
# print(imapObj.list_folders()) # 查看所有文件夹
imapObj.select_folder('INBOX', readonly=True)  # 选择文件夹
print(imapObj.search([u'SINCE', u'01-Jan-2022']))  # 查看指定日期之后的邮件