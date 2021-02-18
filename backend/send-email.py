## require pip install schedule
import schedule
import time
import json
import os
import sqlite3
import smtplib
import requests

from email.message import EmailMessage
from sqlite3 import Error

def create_conn():
    current_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.join(current_path, 'superdb.db')
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def query_email(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscriber")
    rows = cur.fetchall()
    return rows

def get_fortune():
    re = requests.get("http://yerkee.com/api/fortune/all")
    fine = json.loads(re.content)
    return str(fine["fortune"])

def send_email(subject, message, destination):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('toonkunggs@gmail.com', 'gvtmqzqtwhwhdpjh')
        msg = EmailMessage()
        message = f'{message}\n'
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = 'toonkunggs@gmail.com'
        msg['To'] = destination
        server.send_message(msg)
    except Error as e:
        print(e)

def send_email_to_subsctiber():
    emails = query_email(create_conn())
    for email in emails:
        email = str(email)
        message = get_fortune()
        send_email('Your fortune cookie today', message, email[2:len(email)-3])
    
schedule.every().day.at("08:00").do(send_email_to_subsctiber)

while True:
    schedule.run_pending()
    time.sleep(60)
