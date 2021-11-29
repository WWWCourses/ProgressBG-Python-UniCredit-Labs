# # --------------------------------- list type -------------------------------- #
# clients = ['ivan', 'asen', 'maria']
# clients[0]='ada'

# print( clients )

# # -------------------------------- tupple type ------------------------------- #
# customers = ('ivan', 'asen', 'maria')
# t1 = (9,)
# print( type(t1) )
# x = (9)
# print( type(x) )


# # print( 3*(4+3) )


# # -------------------------------- range type -------------------------------- #
# r = range(0,-5, -1)
# l = list(r)
# print(l)

# 0, -2, -4, -6
# for i in range(0, -7, -2):
# 	print(i)


# print( list(range(2, 10, 2)) )

# l1 = list(range(1,4))
# l2 = list(range(4,10))
# print(l1+l2)


# ----------------------------- common operations ---------------------------- #
# l1 = [1,2,3]
# x = 2

# print( x in l1 )
# print( x not in l1 )

# print( 8 in range(1,8))

# --------------------------------- indexing --------------------------------- #
# l = [1,2,3,9,2,3]
# # print(l[-1])
# # print(l[-2])
# # print(l[-3])

# # index = len(l)-1
# # print( index )
# # print( l[index])

# print(l[-1])


# ---------------------------------- slicing --------------------------------- #
t = (1,2,3,4,5)
# sliced = sequence[start:end:step]
# s = t[0:2]
# print(s)

# s = t[2:6]
# s = t[2:]
# print(s)

# s = t[0::2]
# print(s)

# TASK: slice last 2 elements:
# print( t[-1:-3:-1] )
# print(t[-2:])

# --------------------------------- for loop --------------------------------- #
# t = (1,2,3,4,5)

# for el in t:
# 	print( el )

name = 'abc'
print(name[0])

for index in range(len(name)):
	print( name[index] ,index)






