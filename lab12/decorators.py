# def stars_decorator(f):
# 	def wrapper(user):
# 		print("*" * 50)
# 		f(user)
# 		print("*" * 50)

# 	return wrapper


# @stars_decorator
# def greet(user):
# 	print(f"Howdy {user}!")


# let's decorate greet:
# greet = stars_decorator(greet)

# greet('Ada')
# greet('Pesho')


# def increase_balance(value):
# 	print(value)

# def function_maker(f):

# 	def wrapper(param):
# 		print('log....')
# 		f(param)

# 	return wrapper

# increase_balance(10)

# # now, when increase_balance is called, we want to add log

# increase_balance = function_maker( increase_balance )

# increase_balance(10)
# increase_balance(10)
# increase_balance(10)


def log_decorator(f):
	def wrapper(x,y):
		print(f'x = {x}, y = {y}')

		return f(x,y)

	return wrapper


def add(x,y):
	if y==0:
		return 1
	else:
		return x+y

print( add(2,0) )

add = log_decorator(add)

print( add(2,0) )
