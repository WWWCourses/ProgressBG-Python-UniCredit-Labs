# ------------------------ procedural programming demo ----------------------- #
# def drive_car(car):
# 	print(f'{car["model"]} is driving with {car["speed"]}')

# def drive_motor(motor):
# 	drive_car(motor)

# car1 = {
# 	'color': 'red',
# 	'model': 'ford',
# 	'age': 1998,
# 	'speed': 240
# }


# model = 'bmv'
# car['model'] = model

# car2 = {
# 	'color': 'black',
# 	'model': 'BMV',
# 	'age': 1998,
# 	'sped': 220
# }


# motor = {
# 	'model': 'BMV',
# 	'age': 1998,
# 	'sped': 220
# }

# drive_car(car1) # 'ford is driving with 240'
# drive_car(car2) # 'BMV is driving with 220'

# --------------------------------- OOP demo --------------------------------- #
# CAR:
# attributes:
# 	color: string
# 	model: sring
# 	age: numbers
# 	speed: number
# method:
#   drive()

class Car:
	# class attribute
	color='red'

	# define object(instance) attributes:
	def __init__(self, color, model, age, speed):
		print('Car Constructor is invoked!')
		self.color = color
		self.model = model
		self.age = age
		self.speed = speed

	# instance method
	def drive(self):
		print(f'{self.model} is driving with {self.speed}')

# create instances of class Car:
car1 = Car('red','ford', 1998, 240)

car_data = {
	'color': 'blue',
	'model': 'bmv',
	'age': 2004,
	'speed': 300
}
car2 = Car(**car_data )

# use object
car2.drive()
car1.drive()

# change car1 speed to 200
car1.speed = 200
car1.drive()

# RAM:
# # car1.color:222222=> 'red'
# # car1.model:333333=> 'ford'

# # car2.color:324343=> 'blue'
# # car2.model:333333=> '240'


