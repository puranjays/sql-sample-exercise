import sqlite3

with sqlite3.connect("inventory.db") as connection:
	c = connection.cursor()
	c.execute("""SELECT DISTINCT
		inventory.vehicle, orders.order_no, inventory.price FROM inventory, orders
		WHERE inventory.vehicle = orders.model ORDER by 
			orders.order_no ASC""")

	rows = c.fetchall()
	for r in rows:
		print "Model: " + r[0]
		print "Number of orders: " + str(r[1])
		print "Price: " + str(r[2])
		print