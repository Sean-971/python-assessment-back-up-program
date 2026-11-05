#!/usr/bin/python3

"""
This Python code demonstrates the following features:

* send an email using the elasticemail.com smtp server.

"""

import smtplib

smtp = {"sender": "seanythelad@gmail.com",    # elasticemail.com verified sender
        "recipient": "30029394@students.sunitafe.edu.au", # elasticemail.com verified recipient
        "server": "smtp.elasticemail.com",      # elasticemail.com SMTP server
        "port": 2525,                           # elasticemail.com SMTP port
        "user": "seanythelad@gmail.com",      # elasticemail.com user
        "password": "AAAABBBBXXXXYYYYZZZZ"}     # elasticemail.com password

# append all error messages to email and send
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")

# main function
def main():
    """
    This Python code demonstrates the following features:
    
    * send an email using the elasticemail.com smtp server.
    
    """
    sendEmail("ERROR: The program has crashed!")

if __name__ == "__main__":
    main()