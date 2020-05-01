
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
# Header
message["from"] = "Inoussa Mouiche"
message["to"] = "nsangouinoussa515@gmail.com"
message["subject"] = "This is a test from Python"

# body
body = template.substitute({"name": "Inoussa"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("tst.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("nsangouinoussa515@gmail.com", "pwd")
    smtp.send_message(message)
    print("sent...")
