from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class SendSMS():

    def send_sms(self, number, msg_body):
        num = (f'+1{number}')
        client = Client()
        message = client.messages.create(
            to=num, from_="+12059272579", body=msg_body)

if __name__ == "__main__":
    sms_sender = SendSMS()
    sms_sender.send_sms("6099377475", "Test Message please don't respond")