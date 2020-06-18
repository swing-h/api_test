import smtplib
from email.header import Header  # 用于使用中文邮件主题
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.mime.text import MIMEText
from api_test_framework.config.config import *

def send_email(report_file):
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = '18303014261@163.com'  # 发件人
    msg['To'] = 'zhaoyahao@situdata.com'  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # 参数化一下report_file
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # 从配置文件中读取
        smtp.login(smtp_user, smtp_password)  # 从配置文件中读取
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()