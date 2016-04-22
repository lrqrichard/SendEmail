#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(),addr))

#Email addr and pwd
from_addr = input('From: ')
password = input('Password: ')
#Receiver email addr
to_addr = input('To: ')
#SMTP server
smtp_server = input('SMTP server: ')
smtp_port = 25 #25 is the default port without ssl

msg = MIMEText('I am sending you the mail','plain','utf-8')
msg['From'] = _format_addr('Alex <%s>' % from_addr)
msg['To'] = _format_addr('You <%s>' % to_addr)
msg['Subject'] = Header('I love you','utf-8').encode()

server = smtplib.SMTP(smtp_server,smtp_port)
#server.starttls() #only when ssl is used
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()