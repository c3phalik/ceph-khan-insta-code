# Author: @cephkhan (Ceph A. Khan)

# PYTHON SCRIPT TO READ EMAILS USING imaplib MODULE

# IMAP is an email retrieval protocal which has permissions # to only read and display emails.
# We will create a client for communicating with IMAP
# servers

# Importing dependencies

import email
import imaplib

# Defining a method to check inbox for new emails


def check_new_email():
    try:
        # Connecting to SMTP Server over SSL using IMAP Module
        gmail = imaplib.IMAP4_SSL("imap.gmail.com")

        # Logging into the email account using credentials
        gmail.login("YOUR_EMAIL", "YOUR_PASS")

        # Select INBOX from email & set readonly flag to True to prevent modifications
        gmail.select("INBOX", readonly=True)

        # Search Inbox for emails (First argument charset set to None)
        # Use destructuring to store list of mail ids in mail_ids variable
        response, mail_ids = gmail.search(None, 'ALL')

        # Split the mail id and storing the first & last ids in respective variables
        ids_list = mail_ids[0].split()
        first_email_id = int(ids_list[0])
        last_email_id = int(ids_list[-1])

        # Iterating through the list of emails
        for i in range(last_email_id, first_email_id, -1):
            # Fetching email with id 'i' using RFC822 Protocol
            # Returned data: List containing email details
            typ, data = gmail.fetch(str(i), '(RFC822)')

            # Iterating through each item in the data list
            for each in data:
                # Checking if each is an instance of tuple
                if isinstance(each, tuple):
                    # Return the message object structure from bytes.
                    msg = email.message_from_bytes(each[1])

                    # Fetching and storing Subject, Sender, and Date form the message object
                    subject = msg["Subject"]
                    sender = msg["From"]
                    date = msg["Date"]
                    print(f'Subject: {subject}, From: {sender}, Date: {date}')

    except imaplib.IMAP4.error as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    check_new_email()