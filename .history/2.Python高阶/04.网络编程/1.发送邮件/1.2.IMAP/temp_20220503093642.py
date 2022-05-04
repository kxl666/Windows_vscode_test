import pprint
import imaplib
import imapclient
import pyzmail

imaplib._MAXLINE = 10000000
imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
imapObj.login('2244951869@qq.com', 'eezkyozvtsgpdjad')
# print(imapObj.list_folders()) # 查看所有文件夹
imapObj.select_folder('INBOX', readonly=True)  # 选择文件夹
UIDs = imapObj.search(['SINCE 02-May-2022',
                       'FROM 2244951869@qq.com'])  # 查看指定日期之后的邮件

rawMessages = imapObj.fetch([1593], ['BODY[]', 'FLAGS'])  # 查看指定邮件
message = pyzmail.PyzMessage.factory(rawMessages[1593][b'BODY[]'])  # 解析邮件
print(message.get_subject())  # 查看邮件主题

print(message.get_addresses('from'))  # 查看发件人
print(message.get_addresses('to'))  # 查看收件人
# print(message.get_addresses('cc'))  # 查看抄送人
# print(message.get_addresses('bcc'))  # 查看密送人
# print(message.get_addresses('reply-to'))  # 查看回复人
# print(message.get_addresses('sender'))  # 查看发件人
# print(message.get_addresses('resent-from'))  # 查看转发人
# print(message.get_addresses('resent-to'))  # 查看转发收件人
# print(message.get_addresses('resent-cc'))  # 查看转发抄送人
# print(message.get_addresses('resent-bcc'))  # 查看转发密送人
# print(message.get_addresses('resent-reply-to'))  # 查看转发回复人
# print(message.get_addresses('resent-sender'))  # 查看转发发件人

# print(message.text_part)  # 查看邮件正文

# rawMessages = imapObj.fetch(UIDs, ['BODY[]'])  # 查看指定邮件
# pprint.pprint(rawMessages)
# pprint.pprint(message.html_part)  # 查看邮件正文
# pprint.pprint(message.text_part)  # 查看邮件正文
pprint.pprint(message.text_part.get_payload().decode.text_part.cha)  # 查看邮件正文
imapObj.logout
