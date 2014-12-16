import sqlite3
import csv

with sqlite3.connect("employees.db") as connection:
	c = connection.cursor()
	employees = csv.reader(open("employees.csv", "rU"))
	c.execute("""CREATE TABLE employees(name TEXT, position TEXT, salary INT)""")
	c.executemany("INSERT INTO employees(name, position, salary) values (?, ?, ?)", employees)