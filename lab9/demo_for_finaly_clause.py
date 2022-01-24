def insert_into_users(user,age):
	print('open DB connect')
	if(x):
		print(f'data inserted!')

def close_db():
	print('DB connetion closed!')

try:
	insert_into_users('maria', 23)
	print('try end')
except Exception as e:
	print(f'Ooops, something went wrong! ({e})')
	exit(0)
else:
	print('Thank you in else!')
	exit(0)
finally:
  close_db()

close_db()

print('Program continues....')