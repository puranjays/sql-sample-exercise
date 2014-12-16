import sqlite3

with sqlite3.connect("newnumber.db") as connection:
	c = connection.cursor()
	choices = {"AVG":"SELECT avg(num) FROM numbers",
				"MIN":"SELECT min(num) FROM numbers",
				"MAX": "SELECT max(num) FROM numbers",
				"SUM": "SELECT sum(num) FROM numbers"
				}
	print "What would you like to do with the data?"
	print "1. AVG: Get average of all numbers"
	print "2. MIN: Get the smallest of all numbers"
	print "3. MAX: Get the largest of all numbers"
	print "4. SUM: Get the sum of all numbers"
	print "Please enter your choice:"
	user_input = raw_input("> ")

	if user_input == "1":
		c.execute(choices.values()[0])
		results = c.fetchall()
		print results[0]