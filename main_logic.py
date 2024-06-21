import  smtplib
import os
from dotenv import load_dotenv
import datetime
#from email.mime.text import MIMEText
# Load the local .env file to be used
load_dotenv('.env')

def send_plan(date:str, location:str, note:str):
    # Defining some variables
    sender_email = str(os.environ.get('SENDER_EMAIL'))
    email_passkey = str(os.environ.get('EMAIL_PASSKEY'))
    # Temp solution
    recipient_emails = [str(os.environ.get('RECIPIENT_EMAILS'))]

    # Create and start a SMTP server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    # Login to the sender's email account
    server.login(sender_email, email_passkey)

    # Construct the message to be sent
    msg = f"Subject: Random hangout plan\n\nGreetings,\nYou are invited to a random hagout with the members of the society,\nThe hangout will take place on {date}, at {location}, We are excited to see you there!\n\nNote: -{note}-\n\n\n The Planning Division."

    # Send email
    server.sendmail(sender_email,recipient_emails,msg)
    print("Mail sent!")

send_plan("25/6 at 8-PM", "The School", "bring your bikes, we will race!")