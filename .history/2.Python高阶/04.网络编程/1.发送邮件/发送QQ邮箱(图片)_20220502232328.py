import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_sender = '2244951869@qq.com'  # 发件人邮箱账号
my_pass = 'eezkyozvtsgpdjad'  # 发件人邮箱密码
my_user = '2244951869@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:

        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = Header("柯小乐", 'utf-8')
        msgRoot['To'] = Header("测试", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        mail_msg = """
          <p>Python 邮件发送测试...</p>
          <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
          <p>图片演示：</p>
          <p><img src="cid:image1"></p>
          """

        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 指定图片为当前目录
        fp = open(r'C:\Users\kxl666\Desktop\', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        # 以下连接QQ邮箱smtp服务器
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [
            my_user,
        ], msgRoot.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
