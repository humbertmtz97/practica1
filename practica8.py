#!/bin/bash
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

if __name__ == '__main__':
    print(sys.argv)

data = {}
with open('pass.json') as f:
        data = json.load(f)

msg = MIMEMultipart()

 
message = "Enviado en la madrugadaa las 4:00 am del 1/05/21"

  

msg['From'] = data['user']
receipents = ["humbertmtz97@outlook.es"]
msg['To'] = ", ".join(receipents)
msg['Subject'] = "Salu2crack"

 

msg.attach(MIMEText(message, 'plain'))

 
server = smtplib.SMTP('smtp.office365.com:587')

 

server.starttls()

 
server.login(data['user'], data['pass'])

 

server.sendmail(msg['From'], receipents, msg.as_string())

 

server.quit()

 

print("successfully sent email to %s:" % (msg['To']))
