import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os.path
# Define email sender and receiver
email_sender = 'mohamed.helalll.123.poo@gmail.com'
email_password = 'eqiedhkexylkfzmv'
email_receiver = 'mahmoud.ahmad.hamed@gmail.com'

# Set the subject and body of the email
subject = 'Check out my new video!'
content = """
Hello ITI
"""

em = MIMEMultipart()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
body = MIMEText(content, 'plain')
em.attach(body)

filename = 'test.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=os.path.basename(filename))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(filename))
em.attach(part)


# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())