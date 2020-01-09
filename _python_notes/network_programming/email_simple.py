#!/usr/bin/env python

# Module for sending email
import smtplib

"""
Sending e-mail
    import smtplib module
    Create an SMTP object specifying server
    Call sendmail() method from SMTP object
    Recipient list should be a list or tuple, or could be a plain string containing a single recipient
"""
DEBUG = True # set to false for production

smtp_user = 'jstrickpython'
smtp_pwd = 'python(monty)'

sender = 'jstrick@mindspring.com'
recipients = ['jstrickler@gmail.com']
msg = '''Subject: SMTP example
Hello hello?
Testing email from Python
'''

# Connect to SMTP server
smtpserver = smtplib.SMTP("smtpcorp.com", 2525)

# Log into SMTP server
smtpserver.login(smtp_user, smtp_pwd)

# Turn on debugging to show exchange with SMTP server
smtpserver.set_debuglevel(DEBUG)

try:
    smtpserver.sendmail(
        sender,
        recipients,
        msg
    )   # Send the message
except Exception as e:
    print("Unable to send mail:", e)
finally:
    # Disconnect from SMTP server
    smtpserver.quit()
