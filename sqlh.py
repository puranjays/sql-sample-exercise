import sqlite3

with sqlite3.connect("newdb.db") as conn:
	c = conn.cursor()

	#update data
	c.execute("UPDATE population SET population = 1000000 WHERE city='New Delhi'")

	c.execute("DELETE FROM population WHERE city='Mumbai'")

	print "\nNEW DATA:\n"

	c.execute("SELECT * FROM population")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]