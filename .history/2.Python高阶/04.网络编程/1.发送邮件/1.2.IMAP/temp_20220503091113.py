import imapclient
import pyzmail

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
imapObj.login('2244951869@qq.com', 'eezkyozvtsgpdjad')
# print(imapObj.list_folders()) # 查看所有文件夹
imapObj.select_folder('INBOX', readonly=True)  # 选择文件夹
print(imapObj.search([u'SINCE', u'01-Jan-2022']))  # 查看指定日期之后的邮件

rawMessages = imapObj.fetch([688], ['BODY[]', 'FLAGS'])  # 查看指定邮件
message = pyzmail.PyzMessage.factory(rawMessages[688][b'BODY[]'])  # 解析邮件
