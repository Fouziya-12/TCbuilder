import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('fouziyapathan12@gmail.com','kwrr ljdn idtw utuc')
    msg=EmailMessage()
    msg['From']='fouziyapathan12@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()