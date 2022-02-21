# def foo():
# 	print('foo')

# x = 1

# print( type(foo) )
# print( type( foo() ) ) #?
# print( type( None ) ) #?
# print( type(x) )

# # foo => function object
# # x   => integer object


# --------------------------- function as argument --------------------------- #
# def greet(name):
# 	print("Hello, {}".format(name))

# # a function can be passed as argument to another function
# def wrapper(f, n):
# 	f(n)

# name = 'ada'
# wrapper( greet , name)

# ------------------------- function as return value ------------------------- #

def foo():
	x = 1
	def bar():
		print('bar')

	return bar


# foo()()

# res = foo()
# res()

# print( type(res) )
