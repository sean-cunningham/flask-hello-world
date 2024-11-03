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


@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://helloworlddb_fv6l_user:NkUYNSrQaEvMx9HYMV81udB0W1cpuADf@dpg-csjupddsvqrc73f0q91g-a/helloworlddb_fv6l")
    cur = conn.cursor()
    cur.execute(
        '''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        '''
    )
    conn.commit()
    conn.close()
    return "Basketball Table Populated"


@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://helloworlddb_fv6l_user:NkUYNSrQaEvMx9HYMV81udB0W1cpuADf@dpg-csjupddsvqrc73f0q91g-a/helloworlddb_fv6l")
    cur = conn.cursor()
    cur.execute(
        '''
        SELECT * FROM Basketball;
        '''
    )
    records = cur.fetchall()
    conn.close()

    response_String = ""
    response_String += "<table>"
    for player in records:
        response_String += "<tr>"
        for info in player:
            response_String += "<td>{}</td>".format(info)
        response_String += "</tr>"
    response_String += "</table>"
    return response_String


@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://helloworlddb_fv6l_user:NkUYNSrQaEvMx9HYMV81udB0W1cpuADf@dpg-csjupddsvqrc73f0q91g-a/helloworlddb_fv6l")
    cur = conn.cursor()
    cur.execute(
        '''
        DROP TABLE Basketball;
        '''
    )
    conn.commit()
    conn.close()
    return "Basketball Table successfully Dropped"
