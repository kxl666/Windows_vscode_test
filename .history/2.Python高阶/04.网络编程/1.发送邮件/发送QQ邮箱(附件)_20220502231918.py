import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_sender = '2244951869@qq.com'  # 发件人邮箱账号
my_pass = 'eezkyozvtsgpdjad'  # 发件人邮箱密码
my_user = '2244951869@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("柯小乐教程", 'utf-8')
        message['To'] = Header("柯小乐test", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是柯小乐Python 邮件发送测试……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(
            open(r'C:\Users\kxl666\Desktop\Python\2.Python高阶\test.txt',
                 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        message.attach(att1)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [
            my_user,
        ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
