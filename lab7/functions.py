# def make_pancake():
# 	''' this function is making pancakes '''
# 	# this function is making pancakes
# 	print('1. get eggs')
# 	print('2. ....')
# 	print('3. .....')

# def greet():
# 	"""Just prints hello"""
# 	print('~'*20)
# 	print("Hello!")
# 	print('~'*20)

# greet()
# greet()
# greet()
# greet()

# def greet(user_last_name, user_name="Anonymous"):
# 	# user_name = 2+3
# 	"""Just prints hello"""
# 	print('~'*20)
# 	print(f'Hello, {user_name} {user_last_name}')
# 	print('~'*20)

# greet( 'Petrov', 'Pesho' )
# greet( 'Petrov' )

# greet()


# ----------------------------- keyword arguments ---------------------------- #
# def greet(user_last_name, age):
# 	print('~'*20)
# 	print(f'Hello, {user_last_name} you are {age} years old')
# 	print('~'*20)

# greet(age=23, user_last_name='Byron')


# ----------------------------------- *args ---------------------------------- #
def add(*t):
	# t= (2,3)
	# print(t)
	print(sum(t))

add(2,3)
add(2,3,4)



