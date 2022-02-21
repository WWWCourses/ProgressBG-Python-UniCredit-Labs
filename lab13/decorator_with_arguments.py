def star_decorator(f):
	def wrapper(name):
		print('*' * 20)
		f(name)
		print('*' * 20)

	return wrapper

@star_decorator
def greet(name):
	print("Howdy {}!".format(name))


# greet('Ada')
# greet('Pesho')
# greet('Maria')

# greet = star_decorator(greet)

greet('Ada')
greet('Pesho')
greet('Maria')