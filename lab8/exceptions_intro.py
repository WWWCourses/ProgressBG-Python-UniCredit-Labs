# this is not Exception
# print('5)

# this is Exception
# print(x)


x = 1


try:
	y = int(input('y='))
	print(x/y)
except ValueError:
	print('ValueError')
except ZeroDivisionError:
	print('ZeroDivisionError')

print('END')