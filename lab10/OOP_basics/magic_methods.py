class A:
	def __init__(self,id):
		self.id = id

	# def __str__(self):
	# 	return f"id={self.id}"

	def __repr__(self):
		print('repr is called')
		return f"""
			# This is representation of an object:
			obj = A()
			obj.id = {self.id}
		"""
obj1 = A(1)

print(obj1)



# obj1.__str__()