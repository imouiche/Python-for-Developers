from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
client.messages.create(
    to="+12502172800",
    from_="+17622043955",
    body="This is a Python program test from Inoussa Nsangou 😄"
)