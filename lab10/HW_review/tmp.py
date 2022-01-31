# d = {
# 	'id':1
# }

# print(d)


# x = 4

# def foo():
# 	pass
# class A:
# 	pass

# a = A()

# names = {
# 	'x': x,
# 	'foo': foo,
# 	'A': A,
# 	'a':a
# }

# A.id = 1
# print(A.id)

# names['A'].id = 9

# print(names['A'].id)
# print(A.id)


# a1 = names['A']()



# print(id(x))
# print(id(foo))
# print(id(A))
# print(id(a))
# # RAM:
# # 	GLOBAL = {
# # 		x:9789088 => 0010,
# #			a:140178246413088 =>0101010101010
			# A: 8985989:
# # 	}




x = 4
y = x
x = 9
y = 8

print(y)

# Are numbers mutalble?
# RAM:
# 	   11111 => 4
# 	x: 22222 => 9
# 	y: 33333 => 8