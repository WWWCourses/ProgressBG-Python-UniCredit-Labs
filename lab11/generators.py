# for el in [1,2,3]:
# 	print(el)

# for el in range(1,4):
# 	print(el)



def foo_generator():
	print('generator start')
	yield 1
	yield 2
	yield 3
	yield 2
	yield 2
	print('generator end')

foo_gen = foo_generator()

for x in foo_gen:
	if x==3:
		break

	print(x)