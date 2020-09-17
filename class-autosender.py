from datetime import datetime
import numpy as np
import smtplib
import re
import time as t
import webbrowser

Advisory = 'http://examplezoomlink.com'
Humanities = 'http://examplezoomlink.com'
French = 'http://examplezoomlink.com'
English = 'http://examplezoomlink.com'
Science = 'http://examplezoomlink.com'
Math = 'http://examplezoomlink.com'
Design = 'http://examplezoomlink.com'
PHE = 'http://examplezoomlink.com'
Music = 'http://examplezoomlink.com'
IBC = 'http://examplezoomlink.com'
ManageBac = 'http://*.managebac.com/' #REPLACE THIS LINK WITH YOUR SCHOOL'S MANAGEBAC LINK
Classroom = 'https://classroom.google.com/'
Drive = 'https://drive.google.com/'


# Add all your holidays here
holidays = []

# Assuming 2020-09-14 is Day 1
start_date = '2020-09-11' #Set this to this the first day of your cycle
today = np.busday_count(start_date, np.datetime64('today'), holidays=holidays) % 8 + 1 #Set 8 
now = datetime.now()
t_string = now.strftime("%H:%M")	
time = re.sub(":","",str(t_string))
time = int(time)
print(time)
day = datetime.today().weekday()
print(day)
if day != 2: #NON-WEDNESDAY SCHEDULES Our school has a differently timed schedules on Wednesdays 'Teacher Development'.
    if 0 < time < 925: #8:00 - 9:25
        classes = {
            1: 'Humanities', #1st class day 1
            2: 'French', #1st class day 2
            3: 'Independent', #1st class day 3
            4: 'Music', #etc...
            5: 'English',
            6: 'Science',
            7: 'Design',
            8: 'Math',
        }
        current_class = classes[today]
    if 925 < time < 1105:
        classes = { 
            1: 'Wellbeing', #2nd class day 1
            2: 'PHE', #2nd class day 2
            3: 'English',
            4: 'Science',
            5: 'PHE',
            6: 'Math',
            7: 'Humanities',
            8: 'French',
        }
        current_class = classes[today]
    if 1105 < time < 1245:
        classes = { #dict for what classes I have as second period on days 1-8
            1: 'English',
            2: 'Science',
            3: 'Design',
            4: 'Math',
            5: 'Humanities',
            6: 'French',
            7: 'Independent Working Time',
            8: 'Music',
        }
        current_class = classes[today]
    if 1245 < time <= 1500:
        classes = {
            1: 'Design',
            2: 'Math',
            3: 'Humanities',
            4: 'French',
            5: 'IBC',
            6: 'Music',
            7: 'English',
            8: 'Science',
        }
        current_class = classes[today]
    if 1500 < time:
        current_class = 'Nothing'
else: # WEDNESDAY SCHEDULES
    if 0 < time < 900: #Midnight - 9:25
        classes = {
            1: 'Humanities',
            2: 'French',
            3: 'Independent',
            4: 'Music',
            5: 'English',
            6: 'Science',
            7: 'Design',
            8: 'Math',
        }
        current_class = classes[today]
    if 900 < time < 1015:
        classes = {
            1: 'Wellbeing',
            2: 'PHE',
            3: 'English',
            4: 'Science',
            5: 'PHE',
            6: 'Math',
            7: 'Humanities',
            8: 'French',
        }
        current_class = classes[today]
    if 1015 < time < 1100:
        current_class = 'Advisory'
    if 1100 < time < 1215:
        classes = {
            1: 'English',
            2: 'Science',
            3: 'Design',
            4: 'Math',
            5: 'Humanities',
            6: 'French',
            7: 'Independent Working Time',
            8: 'Music',
        }
        current_class = classes[today]
    if 1215 < time < 1410:
        classes = { 
            1: 'Design',
            2: 'Math',
            3: 'Humanities',
            4: 'French',
            5: 'IBC',
            6: 'Music',
            7: 'English',
            8: 'Science',
        }
        current_class = classes[today]
if time > 1500:
    current_class = 'Nothing'

classes = {
    'Humanities': Humanities,
    'French': French,
    'English': English,
    'Science': Science,
    'Math': Math,
    'Design': Design,
    'PHE': PHE,
    'Music': Music,
    'IBC': IBC,
    'Independent': '',
    'Advisory': Advisory,
    'Nothing': ''
}
currentlink = classes[current_class]

print(currentlink) #Print current link
print(current_class) #Print Current Class
webbrowser.open(currentlink, new=0, autoraise=True)
if time < 1600:
    receivers = ['rhijjawi@isumail.ac.ug','ramzihijjawi@gmail.com','23alannad@isumail.ac.ug','bkalksma@isumail.ac.ug','tkalksma@isumail.ac.ug','']
    sender = '*' #Use your email
    gmail_pass = '*' #use google's app specific passwords so that if this script is compromised it cannot be used to access your email.
    message = f"""From: Automated Class Reminder <{sender}> 
To: Careless Student <(genericrecipient@domain.com)>
Subject: {current_class} is soon!

"""
    
    message += f"You have {current_class} soon. I'll just leave your class's zoom link right here ;) :\n"
    message += f"{currentlink}"
        if current_class == 'Nothing':
        message += f"You are free from school, enjoy the evening"
    message += f'\nHere are a few useful links:\n'
    message += f'{Drive}\n{ManageBac}\n{Classroom}\nThis is an automated message, please send all queries to rhijjawi@isumail.ac.ug'
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(sender, gmail_pass)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        print("Successfully sent email")
    except SMTPException:
        print("Error: unable to send email")
    print(message)
