import sqlite3

conn = sqlite3.connect("newdb.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

conn.close()