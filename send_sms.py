# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = os.environ['twilio_account_sid']
auth_token = os.environ['twilio_auth_token']
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+18559381816",
  to="+14235064850"
)

print(message.sid)