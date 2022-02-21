# name definitions
def greet(name):
	print(f'Hello {name}!')

PI = 3.14



# 'helper_module' : {
# 	'greet': function,
# 	'PI': float
# }

# run only when helper_module is executed as standalone
if __name__ == '__main__':
	print('helper_module executed')
