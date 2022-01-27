

def foo():
	global counter

	if counter<=2:
		print('hi')
	else:
		print(None)

	counter+=1


counter = 1

foo()	# hi
foo()	# hi
foo()   # None