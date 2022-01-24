class A:
	# static(class) attributes
	id = 0

	# class methods
	@classmethod
	def increment_id(cls):
		cls.id+=1

	# static methods
	@staticmethod
	def foo():
		print('static method called')


	# instanse methods
	def bar(self):
		print('instanse method called')

a1 = A()
a2 = A()

# call class method
A.increment_id()
A.increment_id()
A.increment_id()
print(A.id)

# instances have acces to class methods
a1.increment_id()
print(A.id)

# call static methods
A.foo()

# object_name.attribute_name = something
# a1.name = 'a1'
# a1.id = 1


# A.id = 99
# print(A.id)
# print(a1.id)


