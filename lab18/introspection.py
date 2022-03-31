# class A:
# 	def __init__(self,x):
# 		self.x = x

# 	def __repr__(self):
# 		return f'x: {self.x}'


# obj =  A(1)
# print(obj)

# print( obj.__dir__() )
# print('~'*20)
# print( dir(obj) )

# print( type(obj) )
# print( type(2) )


# x = 1
# y = 1

# print( id(x) )
# print( id(y) )


# class A:
# 	def __init__(self,x):
# 		self.x = x

# 	def __repr__(self):
# 		return f'x: {self.x}'


# obj=A(1)
# print( hasattr(obj, 'x') )
# setattr(obj, 'x', 99)
# print(obj.x)
# print( getattr(obj,'x') )

# print( isinstance(obj, (A,) ))


# import inspect

# def foo():
# 	func_name = inspect.stack()[0][3]
# 	caller_name = inspect.stack()[1][3]
# 	print("I'm {}.\n{} called me!".format(func_name,caller_name) )

# def bar():
# 	foo()

# bar()