import smtplib
import ssl

port = 465 # ssl
smtp_server = 'smtp.gmail.com' # smtp from gmail
# TO DO
sender_mail = 'name@gmail.com'
rec_mail = 'name@gmail.com'
password = 'your password'
# TO DO
message = '''\
subject: title
how are you?
אפשר כמובן לכתוב גם בעברית...
'''

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_mail, password)
    server.sendmail(sender_mail, rec_mail, message)
