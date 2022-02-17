def calc(f, x, y):
	print(f(x,y))


# def add(x,y):
# 	return x+y

# def mul(x,y):
# 	return x*y


# calc( add, 2, 3 )
# calc( mul, 2, 3 )


# calc( lambda x,y: x+y, 2, 3 )
# calc( lambda x,y: x*y, 2, 3 )


# def greet(_):
# 	return print('hi')

greet = lambda _: print('hi')


print( greet(0) )
