import sqlite3
conn=sqlite3.connect('test.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(
    userid INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT);
    ''')
conn.commit()

