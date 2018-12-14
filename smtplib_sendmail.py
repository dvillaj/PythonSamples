import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

#server = smtplib.SMTP('localhost', 1025)

username = 'dvillaj@gmail.com'
password = 'calella13'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)

server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('dvillaj@gmail.com',
                    ['dvillanuevaj@indra.es'],
                    msg.as_string())
finally:
    server.quit()


