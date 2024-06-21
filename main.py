import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Read the data from Excel
# Load data from Excel
data = pd.read_excel('emails.xlsx')
email_col = data.get("Email")
list_of_emails=list(email_col)
print(list_of_emails)

# Email server configuration
smtp_server=smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login("email_id", "password")

# Function to send email
from_ = "email_id"
to_ = list_of_emails
message=MIMEMultipart("alternative")
message['Subject']="This is just a testing message"
message["from"]="email_id"
#Create the text in form of html
html= '''
<html>
<head>

</head>
<body>
      <h1>Email Automation Bot</h1>
    
'''
part2=MIMEText(html,"html")
message.attack(part2)

#Send the message
smtp_server.send(from_, to_, message.as_string())

print("All Messages are sent.")

    
