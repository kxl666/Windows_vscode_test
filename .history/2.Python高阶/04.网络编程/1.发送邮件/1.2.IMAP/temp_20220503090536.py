import imapclient

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
print(imapObj.login('2244951869@qq.com', 'eezkyozvtsgpdjad'))
