# ------------------------ procedural programming demo ----------------------- #
def drive_car(speed):
	print(f'driving with {speed}')


def print_year(year):
	print(f'Year is {year}')


# cars = [
# 	{
# 		'model':'ford',
# 		'year': 2021,
# 		'color': 'red',
# 		'speed': 100,
# 	},
# 	{
# 		'model':'bmw',
# 		'year': 2020,
# 		'color': 'black',
# 		'speed': 200,
# 		'drive': drive_car
# 	},
# ]


# drive(cars[0]['drive']() )
# drive(cars[1]['speed'])

# --------------------------------- OOP demo --------------------------------- #
# 'model':'bmw',
# 'year': 2020,
# 'color': 'black',
# 'speed': 200,
# 'drive': drive_car

class Person:
	name = "Anonymous"
	age = 100

	def greet(self,surname):
		print(surname)
		print(f'Hello, I\'m {self.name} ')


maria = Person()
maria.name = 'Maria'
# maria.greet()
# maria.greet(maria)
maria.greet('Popova')


# pesho = Person()
# pesho.name = 'Petar'
# pesho.greet()


# print(maria.name)
# print(Person.name)


