import mysql.connector
from mysql.connector import connection
import pandas as pd

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
conn = make_connection (user="test", password="test1234", db='test')

with conn.cursor() as c:
	c.execute('create TABLE IF NOT EXISTS products (product_name varchar(20), price int)')
	conn.commit()

	data = {
		'product_name': ['Computer','Tablet','Monitor','Printer'],
		'price': [900,300,450,150]
	}
	df = pd.DataFrame(data, columns= ['product_name','price'])

	# df.to_sql('products', conn, if_exists='replace', index = False)

	# c.execute('''
	# SELECT * FROM products
	#           ''')

	# for row in c.fetchall():
	#     print (row)
