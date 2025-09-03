# sqlite_introduction.py
import sqlite3


with sqlite3.connect("./users.db") as con:
    cur = con.cursor()
    res =cur.execute("SELECT * FROM users")

    for record in res:
        print (record[0], record[1], record[2])






