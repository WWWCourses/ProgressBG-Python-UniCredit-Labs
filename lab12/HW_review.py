class EvensRange:
	def __init__(self,**kw):
		self.start = kw['start']
		self.end = kw['end']
		self.current = self.start-1

	def __next__(self):
		if self.current<self.end:
			self.current+=1
			return chr(self.current)
		else:
			raise StopIteration

		# if self.number <= self.max_count:
		# 	self.number+=1
		# 	return  self.number
		# else:
		# 	raise StopIteration

	def __iter__(self):
		return self

evens_range = EvensRange(start=1040, end=1071)

for i in evens_range:
	print(i,end=' ')