# sqlite_operations.py

# CRUD
# Create
# Retrieve
# Update
# Delete

import sqlite3


with sqlite3.connect("./users.db") as con:

    cur = con.cursor()

    # C - create
    sql = "INSERT INTO users (name, email, active) VALUES('new user', 'new.user@gmail.com', 1)"
    cur.execute(sql)

    # R - retrieve
    sql = "SELECT * FROM users"
    res = cur.execute(sql)

    for record in res:
        print (record)

    # U - update
    sql = "UPDATE users SET name='CHANGED' WHERE Id = 6"
    cur.execute(sql)

    # D - delete
    sql = "DELETE FROM users WHERE id > 6"
    cur.execute(sql)

    # R - retrieve
    sql = "SELECT * FROM users"
    res = cur.execute(sql)

    for record in res:
        print (record)






