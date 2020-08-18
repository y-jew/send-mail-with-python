import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

username = 'username@gmail.com'
password = 'password'
smtp_server = 'smtp.gmail.com' # your smtp server

'''
Two easy-to-use functions for sending emails
'''


def send_mail(text='some Email from python', subject='Hello World', from_email='your name <username@gmail.com>',
              to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host=smtp_server, port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


def send_mail_alone(sender, to, subject, text, html=None):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = to

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    if html:
        part2 = MIMEText(html, "html")
        message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, to, message.as_string())


def main():
    send_mail(to_emails=['email1', 'email2'])
    send_mail_alone('name name <username@gmail.com>', 'recivermail@gmail.com', 'hi', 'some mail from python')


if __name__ == '__main__':
    main()
