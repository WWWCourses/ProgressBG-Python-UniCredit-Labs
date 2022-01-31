class A:
	id = 1
	def __init__(self):
		self.id = 9
		self.foo()
		self.validate_data()

		# pass

	# instance method
	def foo(self):
		print('instance method')

	# class method:
	@classmethod
	def bar(cls):
		cls.id = 10000
		print('class method')

	# static methods
	@staticmethod
	def validate_data():
		print('validate_data')





a = A()

a.foo()
A.bar()
print(A.id)


