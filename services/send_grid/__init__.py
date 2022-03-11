import os
from fusion10.settings import SEND_GRID_TOKEN, EMAIL_TO_SEND_GRID, EMAIL_FROM_SEND_GRID

from sendgrid import SendGridAPIClient


class SendGridServic:

    def __init__(self, subject, content, email):
        self.service = SendGridAPIClient(api_key=SEND_GRID_TOKEN)
        self.email_to = EMAIL_TO_SEND_GRID
        self.email_from = EMAIL_FROM_SEND_GRID
        self.request_body = None
        self.subject = subject
        self.content = content
        self.email = email

    def get_data(self):
        data = {
            "personalizations": [
                {
                    "to": [
                        {
                            "email": "jackson.teruya@gmail.com"
                        }
                    ],
                    "subject": self.subject
                }
            ],
            "from": {
                "email": "test.automacao2021@gmail.com"
            },
            "content": [
                {
                    "type": "text/html",
                    "value": self.content
                }
            ],
            "reply_to": {
                "email": self.email
            }
        }
        self.request_body = data

    def send_email(self):
        self.service.client.mail.send.post(request_body=self.request_body)
