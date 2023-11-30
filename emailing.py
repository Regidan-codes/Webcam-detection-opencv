import smtplib
import os
from email.message import EmailMessage

PASSWORD = os.getenv("PASSWORD")
SENDER = "huberwrat@gmail.com"
RECEIVER = "regidancodes@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'New customer showed up!'
    email_message.set_content("Hey, we just saw a new customer")

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image', subtype="png")

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    pass
