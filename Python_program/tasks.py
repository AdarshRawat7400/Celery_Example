from celery import Celery
from time import sleep
import smtplib
from email.message import EmailMessage
SENDER_EMAIL_ADDRESS = 'ar3357825@gmail.com'
SENDER_EMAIL_PASSWORD = 'yotadota@123'

app = Celery('tasks',broker='redis://localhost:6379/0',backend='db+sqlite:///celery.db') 

@app.task
def reverse(string):
    sleep(5)
    return string[::-1]


@app.task
def email_sender(emails,message):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    msg = EmailMessage()
    msg['Subject'] = 'Regarding change in app policies'
    msg['From'] = SENDER_EMAIL_ADDRESS
    
    

    # Authentication
    print("Authenticating...")
    s.login(SENDER_EMAIL_ADDRESS,SENDER_EMAIL_PASSWORD)
    print("Login Successful")
    msg.set_content(message)
    # sending the mail
    for email in emails:
        msg['To'] = email
        
        s.send_message(msg)
        del msg['To']

    print("Successfully sent email")
    # terminating the session
    s.quit()
        

