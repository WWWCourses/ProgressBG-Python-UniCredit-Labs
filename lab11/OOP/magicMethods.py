class A:
	def __init__(self,id):
		self.id = id
		print('object created')

	# def __str__(self):
	# 	return f'Object with id:{self.id}'

	def __repr__(self):
		print('repr called')
		return f'id:{self.id}'



# create instances
a = A(1)
print(a)


