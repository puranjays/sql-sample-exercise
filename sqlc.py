import sqlite3

conn = sqlite3.connect("newdb.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 250000)")

conn.commit()
conn.close()