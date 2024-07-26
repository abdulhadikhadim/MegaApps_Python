import imghdr
import smtplib
from email.message import EmailMessage
password = "clkbsiqxjgwcbjgv"
EMAIL = "abhadi027@gmail.com"
RECEIVER = "abhadi027@gmail.com"
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer Showed Up!"
    email_message.set_content("Hey, We just saw a new customer")

    with open(image_path,'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype = "image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo
    gmai.starttls()
    gmail.login(EMAIL,password)

    gmail.sendmail(EMAIL,RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path)
