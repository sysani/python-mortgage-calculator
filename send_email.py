from email.mime.text import MIMEText
from decouple import config
import smtplib

password = config('api-pass')

def send_email(email, height, height_average, count):
    from_email="annie@null.net"
    to_email=email
    subject="Height Data"
    message="Your height: <b>%s.</b><br>Average height: <b>%s.</b><br>Total heights counted: <b>%s</b>" % (height, height_average, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    mailserver=smtplib.SMTP('smtp.mail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(from_email,password)
    mailserver.send_message(msg)
