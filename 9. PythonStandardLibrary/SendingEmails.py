# Code is correct, but no output because google prevented VSCode from signing in my
# account

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template
template = Template(Path("Template.html").read_text())

message = MIMEMultipart()
message["from"] = "rishabhrare8@gmail.com"
message["to"] = "srk.harrypotter@gmail.com"
message["subject"] = "Test"
message.attach(MIMEText(template.substitute({"name": "Rishabh"}), "plain"))
# We can also pass name="John" i.e. keyword argument in substitute()
message.attach(MIMEImage(Path("Snapchat-958094804.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("rishabhrare8@gmail.com", "SeekNDestroy")
    smtp.send_message(message)
    print("Sent")
