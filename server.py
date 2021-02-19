import json
import os
import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/email', methods=['POST'])
def index():
    data = json.loads(request.data)
    email = data['email']
    insert(create_conn(), [email])
    return email

def create_conn():
    current_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.join(current_path, 'superdb.db')
    
    try:
        conn = sqlite3.connect(db_file, timeout=10)
    except Error as e:
        print(e)
        
    return conn

def insert(conn, email):
    sql = ''' INSERT INTO subscriber(email)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, email)
    conn.commit()
    conn.close()
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
