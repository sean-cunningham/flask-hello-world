from flask import Flask
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! from Sean Cunningham 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("Hello_WorldDB")
    conn.close()
    return "Database Connection Successful"
