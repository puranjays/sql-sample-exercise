import sqlite3

conn = sqlite3.connect("newdb.db")
cursor = conn.cursor()

try:
	#insert data
	cursor.execute("INSERT INTO population VALUES('Brussels', 'BE', 82000)")
	cursor.execute("INSERT INTO population VALUES('Antwerp', 'IL', 900000)")

	conn.commit()

except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again..."

conn.close()