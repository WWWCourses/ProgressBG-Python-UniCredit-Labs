x = 4
y = x
# del(x)
# print(x)
print(id(x))
x = 100
print(id(x))
print(y)

print( id(x) == id(y) )

# RAM:
# 	: 12398921=> 4
# 	y: 12398921
	# x : 12738832=>100