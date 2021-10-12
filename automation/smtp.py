import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# define a sever with host and port
server = smtplib.SMTP('smtp.gmail.com', 25)

# start
server.ehlo()

# login
server.login('?', '?')

msg = MIMEMultipart()
msg['From'] = 'JieLi'
msg['To'] = 'jz870780@dal.ca'
msg['Subject'] = 'For a Test'

# read the message file
with open('message.txt', 'r') as f:
    message = f.read()

# send message in plain text
msg.attach(MIMEText(message, 'plain'))

# attachment, file should be opened in bytes
filename = 'coding.jpg'
attachment = open(filename, 'rb')

# payload object, process image data
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

# encode image
encoders.encode_base64(p)
p.add_header('content', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mailtest@mail.com', 'jz870780@dal.ca', text)



