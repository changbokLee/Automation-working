from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = "changbok2453@gmail.com"
SMTP_PASSWORD  ="dmdclf4885"

def send_mail(name, addr, subject, contents):
    msg = MIMEMultipart('alternative')

    msg['From'] = SMTP_USER
    msg['TO'] = addr
    msg['Subject'] = name +'님' + subject
    msg['Contents'] = contents

    text = MIMEText(contents, _charset ='utf-8')
    msg.attach(text)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, addr , msg.as_string())
    smtp.close

contents ='''안녕하세요

자동화로 보내지는 메일입니다.'''
send_mail('이창복', 'changbok2453@gmail.com', '자동화메일입니다', contents)