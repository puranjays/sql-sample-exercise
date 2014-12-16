import sqlite3

with sqlite3.connect("inventory.db") as conn:
	c = conn.cursor()
	c.execute("SELECT count(order_no) FROM orders")
	result = c.fetchall()
	for r in result:
		print r[0]