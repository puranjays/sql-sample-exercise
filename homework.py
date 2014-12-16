import sqlite3

with sqlite3.connect("inventory.db") as connection:
	c = connection.cursor()
	inventory_data = [
					('F150', 'Ford', 21000),
					('NSX', 'Nissan', 37000),
					('730d', 'BMW', 80000),
					('Fusion', 'Ford', 18000),
					('Fiesta', 'Ford', 22000),
					('Go', 'Datsun', 14000)]

	c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", inventory_data)
	
	c.execute("UPDATE inventory SET price = 22000 WHERE vehicle = 'F150'")
	c.execute("UPDATE inventory SET price = 38000 WHERE vehicle ='NSX'")

with sqlite3.connect("inventory.db") as conn:
	c= conn.cursor()
	c.execute("SELECT make, price FROM inventory")
	rows = c.fetchall()
	for r in rows:
		print r[0], r[1]