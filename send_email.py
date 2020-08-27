from email.mime.text import MIMEText
from decouple import config
import smtplib

password = config('api-pass')

def send_email(email, location, down, salary, total, count, downpayment_avg):
    from_email="annie@null.net"
    to_email=email
    subject="Real Estate Data"
    message="With a down payment of $<b>%s</b> and a salary of $<b>%s,</b> " % ((f"{down:,}"), (f"{salary:,}"))
    message+="you could afford a $<b>%s</b> home in %s<br>" % ((f"{total:,}"), location)
    message+="<br><br>More Information<br>Out out %s entries, the average down payment is $%s<br>" % (count, (f"{downpayment_avg:,}"))
    #message+="<br>The average salary is $%s<br>" % (salary_avg)
    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    mailserver=smtplib.SMTP('smtp.mail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(from_email,password)
    mailserver.send_message(msg)
