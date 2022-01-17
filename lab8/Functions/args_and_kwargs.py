# def greet(msg, name):
#   print(f"{msg} {name}!")

# greet(name='Maria', msg='Hi')


# --------------------------------- args demo -------------------------------- #
# def add(*x):
# 	print(sum(x))

# add(2,3)
# add(2,3,4)

# -------------------------------- kwargs demo ------------------------------- #
# def greet(x,*args,**kw):
# 	print(x) 	# 1
# 	print(args) # (2,3)
# 	print(kw)	# {}
# 	print(kw['name'])


# greet(1,2,3,name='Maria', age=23)


# ------------------------------ unpacking arguments demo ------------------------------ #
# def greet(age, name):
# 	print(f"Age: {age}, Name: {name}!")

# # data = (23, 'Maria')

# # greet( data[0], data[1])
# # greet( *data)

# data= {
# 	'age':23,
# 	'name': 'maria'
# }

# # greet(data['age'], data['name'])
# greet(**data)
# # greet(name=data['name'], age=data['age'])

# # greet(data['name'], data['age'])






