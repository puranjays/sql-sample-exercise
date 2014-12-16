import sqlite3

with sqlite3.connect("employees.db") as conn:
	c = conn.cursor()

	c.execute("SELECT name, position, salary from employees")

	rows = c.fetchall()

	for r in rows:
		print "{} is the ({}) and he makes ${}".format(r[0], r[1], r[2])