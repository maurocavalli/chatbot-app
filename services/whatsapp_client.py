from twilio.rest import Client

def send_message(account_sid, auth_token, from_number, to_number, body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to_number
    )
    return message.sid

