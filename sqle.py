#executemany() method

import sqlite3

with sqlite3.connect("newdb.db") as connection:
	c = connection.cursor()

	#insert multiple records using a tuple
	cities = [
			('Boston', 'MA', 250201),
			('Houston', 'TX', 800000),
			('Hong Kong', 'HK', 900000),
			('Phoenix', 'AZ', 150000)
			]
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)