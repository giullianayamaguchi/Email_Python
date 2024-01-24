import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'giullianaTavares@outlook.com'
msg['To'] = 'ighordrummond2001@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

with smtplib.SMTP('smtp-mail.outlook.com',587) as mail_server:
    # identify ourselves to smtp gmail client
    mail_server.ehlo()
    # secure our email with tls encryption
    mail_server.starttls()
    # re-identify ourselves as an encrypted connection
    mail_server.ehlo()
    mail_server.login('giullianaTavares@outlook.com', 'Drummond-1208')
    mail_server.sendmail('tavaresgiulliana@gmail.com','ighordrummond2001@gmail.com',msg.as_string())
