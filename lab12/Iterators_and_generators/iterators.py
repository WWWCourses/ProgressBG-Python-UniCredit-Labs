	# l = [1,2,3,4]

# for el in l:
# 	print(el)

class Iterable:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.curr = self.start-1

	def __next__(self):
		if self.curr <= self.end-1:
			self.curr+=1

			return self.curr
		else:
			raise StopIteration

	def __iter__(self):
		return self


iterable1 = Iterable(1,10)

