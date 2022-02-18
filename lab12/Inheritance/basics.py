class Person:
	def __init__(self, name):
		if name:
			self.name = name
		else:
			print('Name is required')
			exit()

	def __str__(self):
		return f"{self.name} is {self.age} years old."

class AcademicPerson(Person):
	def __init__(self, name, course):
		super().__init__(name)
		self.course = course

	def __str__(self):
		return f"name: {self.name}, course:{self.course} "

class Student(AcademicPerson):
	def __init__(self, name, course, score):
		# call the parent class constructor
		super().__init__(name,course)

		self.score = score

	def greet(self):
		print(self)
		print(f"Hi, my name is {self.name} I'm studing {self.course} and my score is {self.score}")

class Teacher(AcademicPerson):
	def __init__(self, name, course, salary):
		# call the parent class constructor
		super().__init__(name,course)

		self.salary = salary

	def greet(self):
		print(f"Hello, my name is {self.name} I'm teaching {self.course} and my salary is {self.salary}")



pesho = Student("Pesho", "Python", 3.5)

# maria = Teacher("Maria", "JS", 3400)
# asen = Person("Maria", 34)

# use objects
# print(asen)

pesho.greet()
# print(maria)

# pesho.greet()
# maria.greet()