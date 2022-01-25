import os
from twilio.rest import Client

account_sid = 'ACb066bcf9c9d5226102dccd80288a38b1'
auth_token = '8391374bda5233789652c76c84e2835a'

client = Client(account_sid, auth_token)
message = client.messages.create(
    to="MY_PHONE_NUMBER",
    from_="+15017122661",
    body="hello"
)

print(message.sid)



