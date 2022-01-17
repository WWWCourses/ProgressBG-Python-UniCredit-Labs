# --------------------------------- example 1 -------------------------------- #
# x = 5

# def foo():
# 	y = 10

# 	def bar():
# 		y = 99
# 		print(f'x in bar:{x}') # ?
# 		print(f'y in bar:{y}')

# 	bar()
# 	print(f'x in foo:{x}')
# 	print(f'y in foo:{y}')

# foo()


# print(f'x in global:{x}') # 5
# print(f'y in global:{y}') # NameError


# RAM:
#  	foo_NAMESPACE{
#      x:12346 => 3
#      y:12348 => 10
#      bar:12322 => function bar
#
#      bar_NAMESPACE:{
#	      y:12346 => 99
#		}
#	}

#
#	GLOBAL_NAMESPACE{
# 		x:12386 => 5
#      foo:12346 => <function foo>
#	}


# 	BUILD_IN_NAMESPACE{
# 		sum: function sum
# 	}

# --------------------------------- Example 2 -------------------------------- #
def outer():
	# x=2

	def inner():
		# x=3
		print(f'x = {x} in inner')

	inner()
	print(f'x = {x} in outer')

# x = 1
outer()
print(f'x = {x} in global')