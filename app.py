from flask import Flask
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! from Sean Cunningham 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://helloworlddb_fv6l_user:NkUYNSrQaEvMx9HYMV81udB0W1cpuADf@dpg-csjupddsvqrc73f0q91g-a/helloworlddb_fv6l")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://helloworlddb_fv6l_user:NkUYNSrQaEvMx9HYMV81udB0W1cpuADf@dpg-csjupddsvqrc73f0q91g-a/helloworlddb_fv6l")
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        '''
    )
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
