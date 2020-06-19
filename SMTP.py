# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def Google_To_En():#Использует SMTP
    # create message object instance
    msg = MIMEMultipart()
     
     
    message = "Thank you"
     
    # setup the parameters of the message
    password = "7830239pf"
    msg['From'] = "yjga657@gmail.com"
    msg['To'] = "makarovtsy1@xn----7sbbfop6bdeyjc6o.xn--p1ai"
    msg['Subject'] = "Subscription"
     
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
     
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
     
    server.starttls()
     
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
     
     
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
     
    print ("successfully sent email to %s:" % (msg['To']))

def En_To_En():#Использует SSL
    # create message object instance
    msg = MIMEMultipart()
         
         
    message = "Thank you"
         
    # setup the parameters of the message
    password = "e1a5753869"
    msg['From'] = "makarovtsy1@xn----7sbbfop6bdeyjc6o.xn--p1ai"
    msg['To'] = "makarovtsy2@xn----7sbbfop6bdeyjc6o.xn--p1ai"
    msg['Subject'] = "Subscription"
         
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
         
    #create server
    server = smtplib.SMTP_SSL('srv.ru: 465')
         
    #server.starttls()
         
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
         
         
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
         
    server.quit()
         
    print ("successfully sent email to %s:" % (msg['To']))
