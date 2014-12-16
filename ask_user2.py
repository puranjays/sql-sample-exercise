import sqlite3

conn = sqlite3.connect("newnum2.db")
cursor = conn.cursor()

prompt = """
Select the operation you want to perform [1-5]:
1. Average of numbers
2. Maximum of numbers
3. Minimum of numbers
4. Sum of numbers
5. Exit the program
"""

while True:
	print prompt
	x = raw_input("> ")
	if x in set(["1", "2", "3", "4"]):
		op = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]
		cursor.execute("SELECT {}(num) FROM numbers".format(op))
		get = cursor.fetchone()
		print op + ": %f" % get
	elif x == "5":
		print "Exit"
		break