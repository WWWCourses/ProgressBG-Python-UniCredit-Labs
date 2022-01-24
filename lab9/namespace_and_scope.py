x = 1

def foo():
	print(f'x in foo: {x}')

	def bar():
		print(f'x in bar: {x}')

	bar()

foo()


print(f'x in gloabl: {x}')


# RAM:
# GLOBAL_NAMESPACE = {
# 	"x":9788992, (1)
#   "foo":140146005876016
# 	FOO_NAMESPACE = {
# 	'	bar': 7382137843 (function)
# 		BAR_NAMESPACE = {
#
# 		}
# 	}


#
