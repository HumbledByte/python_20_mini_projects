from email.message import EmailMessage
import os
import ssl
import smtplib

email_sender = os.environ.get('EMAIL')
email_password = os.environ.get('GMAIL_KEY')

email_receiver = 'radaka2462@dnitem.com'

subject = "Testing out email"
body = """
This is the body of the email
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())