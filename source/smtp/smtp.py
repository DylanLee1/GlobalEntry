from email.mime.text import MIMEText
from dotenv import dotenv_values

import smtplib
import os


def send_email(env_path):
    config = dotenv_values(env_path)

    msg = MIMEText(config['BODY'])
    msg['Subject'] = config['SUBJECT']
    msg['From'] = config['FROM']
    msg['To'] = config['TO']
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(config['FROM'], config['PASSWORD'])
        smtp_server.sendmail(config['FROM'], config['TO'], msg.as_string())
