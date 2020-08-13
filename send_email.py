from email.mime.text import MIMEText
from decouple import config
import smtplib

password = config('api-pass')

def send_email(email, location, down, salary, total):
    from_email="annie@null.net"
    to_email=email
    subject="Real Estate Data"
    message="With a down payment of $<b>%s</b>and a salary of $<b>%s,</b> " % (down, salary)
    message+="you could afford a $<b>%s</b> home in %s" % (total, location)
    #message+="<br>More Information:<br>Average Down Payment:%s<br>Average Salary:%s<br>" % (downpaymnent_avg, salary_avg)
    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    mailserver=smtplib.SMTP('smtp.mail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(from_email,password)
    mailserver.send_message(msg)
