'''
Created on Sep 23, 2017

@author: Eric
'''
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc77a5e1a69d3fb8999521f1dbe926fd9"
# Your Auth Token from twilio.com/console
auth_token  = "30e47ba6be1c2f614b869cdaadd39239"

client = Client(account_sid, auth_token)
clientNum = str(input("enter the number you would like to send a message to"))
clientNum2 = "1" + clientNum 
msg  = str(input("enter the message you would like to send"))
message = client.messages.create(
    to=clientNum2, 
    from_="+18317501029",
    body=msg)

print(message.sid)
print("your message has been sent") 