#mail = imaplib.IMAP4_SSL('imap.gmail.com')
#mail.login('yjga657@gmail.com', '7830239pf')
#mail.enable(capability='UTF8=ACCEPT')
#mail.login("yjga657@gmail.com", "7830239pf")

import imaplib

mail = imaplib.IMAP4_SSL('srv.ru')
mail._mode_utf8()
mail.login("макаровцы1@xn----7sbbfop6bdeyjc6o.xn--p1ai", "e1a5753869")
print('LOGGED')
mail.list()
 
# Выводит список папок в почтовом ящике.
mail.select("inbox") # Подключаемся к папке "входящие".
data = mail.search(None, "ALL")
IDList=data[1]
IDList=IDList[0].split()
LastID=IDList[-1]
print(LastID)

data = mail.fetch(LastID, "(RFC822)")
print(data)
raw_email = data[1][0][1].decode('utf-8')
print(raw_email)

import email
email_message = email.message_from_string(raw_email)
 
print (email_message['To'])
print (email_message['Subject'])
print (email.utils.parseaddr(email_message['From']))
print (email_message.items())

email_message = email.message_from_string(raw_email )
 
if email_message.is_multipart():
    for payload in email_message.get_payload():
        body = payload.get_payload(decode=True).decode('utf-8')
        print(body)
else:    
    body = payload.get_payload(decode=True).decode('utf-8')
    print(body)
