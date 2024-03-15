from flask import send_file
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_message(to: str, message: str) -> None:
    '''
    Send message to a user.
    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send
    Returns:
        - None
    '''

    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )

def send_file_message(to: str, message: str, url: str) -> None:
    '''
    Send file message to a user.
    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send
        - url(str): api url
    Returns:
        - None
    '''

    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to,
        media_url=url.replace('/twilio/receiveMessage', '/getFile')
    )