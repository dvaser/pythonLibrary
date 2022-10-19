import sqlite3 as sql

connection = sql.connect("node_app.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for i in result:
    print(i)

connection.close()