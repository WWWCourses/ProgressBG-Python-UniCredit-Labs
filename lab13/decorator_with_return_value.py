def log_decorator(f):
	def wrapper(x,y):
		print('logging')
		return f(x,y)

	return wrapper


@log_decorator
def add(x,y):
	return x+y

print( add(2,3) )
print( add(5,8) )
print( add(9,12) )

