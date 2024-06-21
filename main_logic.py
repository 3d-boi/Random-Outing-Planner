import  smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv('.env')

def send_plan(title:str, date:str, location:str):
    subject = title
    body = f"On {date}, I think we should go to {location}, It will be fun!"
    sender = os.environ.get('SENDER_EMAIL')
    recipients = os.environ.get('RECEPIENTS_EMAILS')
    email_password = os.environ.get('EMAIL_PASSKEY')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, email_password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

    #print(f"{title}: On {date}, we can go to {location}")

send_plan("Mall outing plan", "27/6", "The mall")