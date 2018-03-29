#!/usr/bin/env python3

import sqlite3

connection=sqlite3.connect('master.db', check_same_thread=False)
cursor=connection.cursor()


cursor.execute("INSERT INTO users(username, password, initialbalance) VALUES('{}', '{}', {});".format("mea", "abc", 10000))
connection.commit()
cursor.execute("SELECT pk from users ORDER BY pk DESC;")




cursor.close()
connection.close()
