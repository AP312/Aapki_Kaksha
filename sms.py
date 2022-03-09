from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACf6a50a07af8d1d6d89eaa607d1f0f4bf'
auth_token = 'aaf9124c9e1d1ea04cf086f65792577e'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Medicine time!!!!',
         from_='+12098864390',
         status_callback='http://postb.in/1234abcd',
         to='+919699472292'
     )

#print(message.sid)