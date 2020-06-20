# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

def Google_To_En():#Использует SMTP
    # create message object instance
    msg = MIMEMultipart()
     
     
    message = "Йоу"
     
    # setup the parameters of the message
    password = "7830239pf"
    msg['From'] = addr_spec="yjga657@gmail.com"
    msg['To'] = "makarovtsy1@xn----7sbbfop6bdeyjc6o.xn--p1ai"
    msg['Subject'] = "Subscription"
     
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
     
    #create server
    server = smtplib.SMTP_SSL('smtp.gmail.com: 465')#587
     
    #server.starttls()
     
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
    msg['Subject'] = "Боже, это ужасно"
         
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

def En_To_Ru():#Использует SSL
    # create message object instance
    #msg = MIMEMultipart()
         
         
    # create message object instance
    msg = EmailMessage()
    msg['Subject'] = "Subj"
    msg['From'] = Address("From", "makarovtsy2", "xn----7sbbfop6bdeyjc6o.xn--p1ai")
    msg['To'] = (Address("To", "макаровцы1", "xn----7sbbfop6bdeyjc6o.xn--p1ai"))
    msg.set_content("""Something """)     
         

    # setup the parameters of the message
         
    # add in the message body
         
    #create server
    server = smtplib.SMTP_SSL('srv.ru: 465')
         
    # Login Credentials for sending the mail
    server.login("makarovtsy2@xn----7sbbfop6bdeyjc6o.xn--p1ai", "bfd20380a6")
         
         
    # send the message via the server.
    server.send_message(msg)     
    server.quit()
         
    print ("successfully sent email to %s:" % (msg['To']))

def Ru_To_Ru():#Использует SSL
    # create message object instance
    msg = EmailMessage()
    msg['Subject'] = "Я обязательно выживу..."
    msg['From'] = (Address("From", "макаровцы2@xn----7sbbfop6bdeyjc6o.xn--p1ai"))
    msg['To'] = (Address("To", "макаровцы1@xn----7sbbfop6bdeyjc6o.xn--p1ai"))
    msg.set_content("""Я обязательно выживу...""")     
         

    # setup the parameters of the message
         
    # add in the message body
         
    #create server
    server = smtplib.SMTP_SSL('srv.ru: 465')
         
    # Login Credentials for sending the mail
    username="макаровцы2@xn----7sbbfop6bdeyjc6o.xn--p1ai"
    server.login(username, "bfd20380a6")
         
         
    # send the message via the server.
    server.send_message(msg)     
    server.quit()
         
    print ("successfully sent email to %s:" % (msg['To']))

