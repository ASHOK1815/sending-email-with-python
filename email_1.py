import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='sender name'
email['to']='email id'
email['subject']='hello there'

email.set_content('I am a python Master')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gmail','password')
    smtp.send_message(email)
    print('all good boss!')

