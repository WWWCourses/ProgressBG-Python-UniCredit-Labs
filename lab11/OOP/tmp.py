d = {'__foo':9}
d['foo'] = 1
print(d)

class A:
	def __init__(self, foo) :
		self.__foo = foo

	def __repr__(self) -> str:
		return f'{self.__foo}, {self.foo}'

a = A(9)
a.foo = 100
print(a)

