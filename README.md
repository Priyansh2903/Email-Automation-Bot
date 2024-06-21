# Email-Automation-Bot

Overview
The Email Automation Bot is a Python-based application designed to automate the process of sending emails using data extracted from an Excel file. This tool is ideal for scenarios where you need to send personalized emails to a large number of recipients efficiently and accurately.

Features
Read Data from Excel: Extracts recipient details and email content from an Excel file.
Send Personalized Emails: Uses the extracted data to send personalized emails to each recipient.
SMTP Integration: Connects to an SMTP server to send emails.
Logging: Keeps a log of sent emails and errors for auditing and troubleshooting purposes.
Requirements
Python 3.6 or higher
pandas library for reading Excel files
openpyxl library for Excel file support
smtplib and email libraries for sending emails
Installation
Clone the Repository:
bash
git clone https://github.com/yourusername/email-automation-bot.git
cd email-automation-bot
Create and Activate a Virtual Environment (optional but recommended):
bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies:
bash

pip install -r requirements.txt
Configuration
Excel File: Prepare an Excel file (emails.xlsx) with the following columns:
Name: Recipient's name
Email: Recipient's email address
Subject: Subject of the email
Message: Body of the email
SMTP Settings: Update the config.py file with your SMTP server details:

Python
SMTP_SERVER = 'smtp.yourserver.com'
SMTP_PORT = 587
SMTP_USER = 'your-email@example.com'
SMTP_PASSWORD = 'your-email-password'
Usage
Run the Script:
bash
python main.py
Log Files: Check the logs directory for logs of sent emails and any errors encountered during the process.

Project Structure
bash
email-automation-bot/
│
├── config.py          # Configuration file for SMTP settings
├── email_bot.py       # Main script to run the email automation
├── requirements.txt   # List of dependencies
├── data.xlsx          # Sample Excel file with recipient details (replace with your file)
├── logs/              # Directory for log files
│   ├── sent.log       # Log file for sent emails
│   └── error.log      # Log file for errors
└── README.md          # Project readme file
Example
Here’s an example of how the emails.xlsx file should look:

Name	      Email	            Subject	        Message
John Doe	  john@example.com	Hello John	    Hi John, How are you?
Jane Smith	jane@example.com	Greetings Jane	Hello Jane, What's up?
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
