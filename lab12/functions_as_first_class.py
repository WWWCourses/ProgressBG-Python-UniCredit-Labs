
def function_maker():

	x = 1

	def greet(name,age):
		print(f'Hello {name}, age={age}')
		print(x)

	return greet



# print(x)
# greet = def greet(name,age):
# 			print(f'Hello {name}, age={age}')
			# print(1)

greet = function_maker()

greet('Ada', 23)
greet('pesho', 12)



# Hello Ada, age: 23