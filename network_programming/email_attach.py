#!/usr/bin/env python

import smtplib
import os

# Class for message body
from email.mime.multipart import MIMEMultipart
# Class for text attachments
from email.mime.text import MIMEText
# Class for image attachments
from email.mime.image import MIMEImage

"""
Email Attachments
    Create MIME multipart message
    Create MIME objects for each of the attachments
    Attach MIME objects
    Serialize message and send
    
    import email.mime
        multipart
            MIMEMultipart for the main message
        text
            MIMEText for text attachments
        image
            MIMEImage for image attachments
        audio
            MIMEAudio for audio attachments
        application
            MIMEApplication for miscellaneous binary data
    
    Once the attachments are created and attached, the message mut be serialize with the as_string() method.
    The actual transport uses smmptlib, just like simple email messages.
"""
SMTP_SERVER = "smtpcorp.com"
SMTP_PORT = 2525
SMTP_USER = 'jstrickpython'
SMTP_PWD = 'python(monty)'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']


# Normal Python script organization
def main():
    smtp_server = create_smtp_server()
    msg = create_message(
        'Here is your attachment',
        'Testing email attachments from python class.',
    )
    add_text_attachment('data/parrot.txt', msg)
    add_image_attachment('data/felix_auto.jpeg', msg)
    send_message(smtp_server, msg)


def create_message(subject, body):
    # Create main message
    msg = MIMEMultipart(body)
    # Set the subject
    msg['Subject'] = subject

    return msg


# Convenience function for attaching text
def add_text_attachment(file_name, message):
    add_attachment(file_name, message, MIMEText, 'r')


# Convenience function to attaching an image
def add_image_attachment(file_name, message):
    add_attachment(file_name, message, MIMEImage, 'rb')


def add_attachment(file_name, message, mime_type, file_mode):
    # Read data for attachment
    with open(file_name, file_mode) as file_in:
        attachment_data = file_in.read()

    short_name = os.path.basename(file_name)
    # Create MIME object of appropriate type
    attachment = mime_type(attachment_data)
    attachment.add_header(
        'Content-Disposition', 'attachment', filename=short_name
    )

    # Attach attachment to main message
    message.attach(attachment)


def create_smtp_server():
    # Connect to SMTP (same as email_simple)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.login(SMTP_USER, SMTP_PWD)

    return smtpserver


def send_message(server, message):
    try:
        server.sendmail(
            SENDER,
            RECIPIENTS,
            message.as_string() # Can't send MIME object; need to convert to string for sending
        )
    finally:
        server.quit()


if __name__ == '__main__':
    main()
