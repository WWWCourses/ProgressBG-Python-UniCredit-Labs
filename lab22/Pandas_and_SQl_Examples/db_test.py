import mysql.connector
from mysql.connector import connection

def make_connection(user, password, db, host="localhost", port=3306):
	try:
		cnx = mysql.connector.connect(
			user=user,
			password=password,
			db=db,
			host=host,
			port=port
		)

	except mysql.connector.Error as e:
		print(e)

	print('Connection Established')
	return cnx


# Connect to server
with make_connection (user="test", password="test1234", db='SimpleCompanyDB') as cnx:
	# Get a cursor
	cur = cnx.cursor()

	# Execute a query
	cur.execute("select * from employee")

	# Fetch one result
	row = cur.fetchall()
	print(row)
