import mysql.connector
from mysql.connector import connection

def make_connection(user, password, db, host="localhost", port=3306):
	try:
		con = mysql.connector.connect(
			user=user,
			password=password,
			db=db,
			host=host,
			port=port
		)

	except mysql.connector.Error as e:
		print(e)

	print('Connection Established')
	return con


# Connect to server
con = make_connection (user="test", password="test1234", db='SimpleCompanyDB')

# # Get a cursor
# cur = con.cursor()

# # Execute a query
# cur.execute("SELECT CURDATE()")

# # Fetch one result
# row = cur.fetchone()
# print("Current date is: {0}".format(row[0]))

# fetch Multiple results
with con.cursor() as cursor:
	cursor.execute(f'SELECT * FROM SimpleCompanyDB.company;')

	results = cursor.fetchall()
	# print(results)
	for r in results:
		print(r)

# Close connection
con.close()

