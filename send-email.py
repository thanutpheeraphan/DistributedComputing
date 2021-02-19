import psycopg2
import smtplib
import requests
import schedule
import json
import time

from email.message import EmailMessage
from sqlite3 import Error

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
    try:
        connection = psycopg2.connect(user="dkklvsxqivphui",
                                          password="19bba5b736bd796a2f70c6703a41a210971b1e5994a9b4b4318ce56e7a803cd9",
                                          host="ec2-3-221-243-122.compute-1.amazonaws.com",
                                          port="5432",
                                          database="d720fio2023gsb")
        cursor = connection.cursor()
        sql = "SELECT * FROM subscriber"
        cursor.execute(sql)
        emails = cursor.fetchall() 
       
        for email in emails:
            email = str(email)
            message = get_fortune()
            send_email('Your fortune cookie today', message, email[2:len(email)-3])
           
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


schedule.every().day.at("08:00").do(send_email_to_subsctiber)
while True:
    schedule.run_pending()
    time.sleep(60)

