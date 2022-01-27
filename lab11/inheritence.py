# class Animal:
# 	def eat(self):
# 		print('eating....')

# class Person(Animal):
# 	"""docstring for Person"""
# 	def __init__(self, name, age):
# 			self.name = name
# 			self.age = age

# 	def greet(self):
# 			print(f"Hi, I'm {self.name}. I'm {self.age} years old.")

# class Employee(Person):
# 	pass

# class Manager(Person):

# 	def greet(self):
# 		print(f"Name: {self.name}. Age: {self.age}")
# 		Person.greet(self)

# 		super().greet()


# pesho = Employee("Pesho",25)
# ivan = Manager("Ivan",45)

# # Employee instances doesn't have any own attributes and methods, but they inherit from their base class - Person.
# # pesho.greet()
# ivan.greet()

# # pesho.eat()


class Animal:
	def eat(self):
		print(f'{self.name} is eating')

class Bird:
	def fly(self):
		print(f'{self.name} is flying')

	def eat(self):
		print(f'{self.name} is eating like a bird')

class Parrot(Animal, Bird):
	def __init__(self, name):
		self.name = name

	def eat(self):
		print('parrot ....')
		# super(Animal, self).eat()


lori = Parrot('Lory')
lori.eat()
# lori.fly()

