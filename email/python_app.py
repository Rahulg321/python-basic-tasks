from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rg5353070@gmail.com'
email_password = 'yavmikaiesurludh'

email_receiver = 'pcterahulbca21b@gmail.com'

subject = 'Take it Easy Rahul! Dont give Up!'

body = """
I know things are difficult and you are feeling a lot of things but its okay, time will pass and with time it will get away
You are a good person, you have your ups and downs but deep down you are a good person, you know it as well as I know it.
Just take it one step at a time and one day at a time, and one second at a time, keep your peace with god!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
