import email.message
import smtplib
import os
from dotenv import load_dotenv
import datetime
import random
import plan_template
import csv
import csvcleaner

# A Temporary list of all the locations available
#locations = ["The School", "The Garden", "The GYM"]

# Recording the current time and date in 2 variables
current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()
min_future_date = current_date + datetime.timedelta(3)

def check_onetime_plans():
    #Clean the past plans
    csvcleaner.clean('Flask Web App/onetime.csv')

    #Cycle throught the remaining plans
    with open('Flask Web App/onetime.csv', 'r') as plans_file:
        csvfile = csv.DictReader(plans_file)
        closest_date = datetime.datetime(5000,12,30,0,0,0).date()
        
        #Plan required info
        plan_date = None
        plan_time = None
        plan_location = None
        plan_note = None

        #Calculates the closest upcoming event
        for num, event in enumerate(csvfile):
            event_date = datetime.datetime.strptime(event['date'],"%Y-%m-%d").date()
            if event_date < closest_date:
                closest_date = event_date
                event_index = num
                plan_date = datetime.datetime.strptime(event['date'],"%Y-%m-%d").date()
                plan_time = datetime.datetime.strptime(event['time'],"%H:%M").time()
                plan_location = event['location']
                plan_note = event['note']
            else:
                continue
            

        
    
    #Sees if the closest upcoming event is far enought to fit another plan in-between it an right now
    if closest_date > min_future_date:
        #Plan is far enough to make another one in the meantime
        generate_random_plan()
    else:
        #Plan is close enought to invite members to
        plan = plan_template.plan(plan_date,plan_time,plan_location,plan_note)
        send_plan(plan)

 
def generate_random_plan():
    # Access the csv files
    with open('Flask Web App/repeating.csv', 'r') as plans_file:
        csvfile = csv.DictReader(plans_file)
        dict_list = list(csvfile)
    random_num = random.randint(0,len(dict_list))

    # Defining some needed variables
    offset_date = current_date + datetime.timedelta(days=random.randint(1,3))
    plan_time = datetime.time(random.randint(17,20),00)
    plan_location = dict_list[random_num]['location']
    plan_note = dict_list[random_num]['note']

    # creating the "plan" object
    plan = plan_template.plan(offset_date,plan_time,plan_location,plan_note)

    # Sending an email with teh generated plan
    send_plan(plan)

def send_plan(plan:plan_template.plan):
    # Load the local .env file to be used
    load_dotenv('.env')

    # Defining some variables
    sender_email = str(os.environ.get('SENDER_EMAIL'))
    email_passkey = str(os.environ.get('EMAIL_PASSKEY'))
    # Temp solution
    recipient_emails = [str(os.environ.get('RECIPIENT_EMAILS'))]

    # Construct and format the message to be sent
    formatted_date = plan.date.strftime("%A %d %b")
    formatted_time = plan.time.strftime("%I:%M %p")

    # Open and read the HTML file, and Replace placeholders with actual values
    with open('email_template.html','r') as html_file:
        msg = html_file.read()
        msg = msg.replace('{date}', formatted_date)
        msg = msg.replace('{time}', formatted_time)
        msg = msg.replace('{location}', plan.location)
        msg = msg.replace('{note}', plan.note)

    # Email data setup
    mail = email.message.Message()
    mail['Subject'] = "SSS Hangout Invitation"
    mail.add_header('Content-Type','text/html')
    mail.set_payload(msg)
    mail_str = mail.as_string()
    

    # Create and start a SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login to the sender's email account
        server.login(sender_email, email_passkey)
        # Send email
        server.sendmail(sender_email,recipient_emails,mail_str.encode('utf-8'))
    
    print("Mail sent!")

check_onetime_plans()