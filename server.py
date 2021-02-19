import psycopg2
import json

from psycopg2 import Error
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/email', methods=['POST'])
def index():
    data = json.loads(request.data)
    email = data['email']
    insert(email)
    return email



def insert(email):
    sql = """INSERT INTO subscriber(email)
             VALUES(%s);"""

    try:
        connection = psycopg2.connect(user="dkklvsxqivphui",
                                      password="19bba5b736bd796a2f70c6703a41a210971b1e5994a9b4b4318ce56e7a803cd9",
                                      host="ec2-3-221-243-122.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d720fio2023gsb")
        cursor = connection.cursor()
        cursor.execute(sql, (email,))
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.commit()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
