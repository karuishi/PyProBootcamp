import os, smtplib
from twilio.rest import Client
from dotenv import load_dotenv

# Using a .env file to retrieve the phone numbers and tokens.
load_dotenv()
class NotificationManager:

    def __init__(self):
        self.smtp_address = os.environ["SMTP_EMAIL_PROVIDER"]
        self.email = os.environ["SMTP_EMAIL"]
        self.email_password = os.environ["SMTP_PASSWORD"]
        self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        #self.connection = smtplib.SMTP(os.environ["SMTP_EMAIL_PROVIDER"])
        
    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(self.email, self.email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )