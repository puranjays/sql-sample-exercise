import sqlite3

with sqlite3.connect("inventory.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE orders(model TEXT, order_no INT, order_date INT)")

	orders = [
				('NSX', 15, 0515),
				('F150', 10, 0614),
				('730d', 5, 0515),
				('Fusion', 55, 1114),
				('Fiesta', 45, 1115)]

	c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

	c.execute("SELECT * FROM orders")
	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]