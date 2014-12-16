import sqlite3

with sqlite3.connect("newdb.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('New Delhi', 'Delhi NCR', 1500000)")
	c.execute("INSERT INTO population VALUES('Mumbai', 'Maharashtra', 1800000)")
