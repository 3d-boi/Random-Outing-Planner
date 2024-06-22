import  smtplib
import os
from dotenv import load_dotenv
import datetime
import random
import plan_template

# A Temporary list of all the locations available
locations = ["The School", "The Garden", "The GYM"]

# Recording the current time and date in 2 variables
current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()
 
def generate_random_plan():
    offset_date = current_date + datetime.timedelta(days=random.randint(1,3))
    plan_time = datetime.time(random.randint(17,20),00)
    plan = plan_template.plan(offset_date,plan_time,"location","note")
    send_plan(offset_date,plan_time,random.choice(locations),"Bring board-games or bikes!")

def send_plan(date:datetime.date, time:datetime.time, location:str, note:str):
    # Load the local .env file to be used
    load_dotenv('.env')

    # Defining some variables
    sender_email = str(os.environ.get('SENDER_EMAIL'))
    email_passkey = str(os.environ.get('EMAIL_PASSKEY'))
    # Temp solution
    recipient_emails = [str(os.environ.get('RECIPIENT_EMAILS'))]

    # Create and start a SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        # Login to the sender's email account
        server.login(sender_email, email_passkey)

        # Construct and format the message to be sent
        formatted_date = date.strftime("%A %d %b")
        formatted_time = time.strftime("%I:%M %p")
        msg = f"Subject: Random hangout plan\n\nGreetings,\nYou are invited to a random hagout with the members of the society,\nThe hangout will take place on {formatted_date}, at {formatted_time}, at '{location}', We are excited to see you there!\n\nNote: -{note}-\n\n\n The Planning Division."

        # Send email
        server.sendmail(sender_email,recipient_emails,msg)
    

    print("Mail sent!")

#send_plan(datetime.datetime.now(), "The School", "bring your bikes, we will race!")
generate_random_plan()