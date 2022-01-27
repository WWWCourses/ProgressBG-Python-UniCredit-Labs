class X:
	def __init__(self,**kw):
		self.number = kw['start'] - 1
		self.max_count = kw['max_count'] -1

	def __next__(self):
		if self.number <= self.max_count:
			self.number+=1
			return  self.number
		else:
			raise StopIteration



	def __iter__(self):
		return self



# define x as Iterator and Iterable
x = X(max_count=4, start=2)

for el in x:
	print(el)