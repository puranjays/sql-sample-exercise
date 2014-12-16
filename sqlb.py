import sqlite3

conn = sqlite3.connect("new2.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO populations VALUES('New York City','NY', '2000000')")
cursor.execute("INSERT INTO populations VALUES('San Francisco','CA', '80000')")

conn.commit()

conn.close()