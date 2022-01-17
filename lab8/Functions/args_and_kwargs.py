# --------------------------------- example 1 -------------------------------- #
# x = 5

# def greet(msg, name):
#   #msg='Maria'
#   #name='Hello'
#   print(f"{msg} {name}!")

# greet('Maria', 'Hello')


# # RAM:
# #       x:1246 => (5)0101
# #   greet:4686 => (function greet)

# #     msg:1246 => ('Maria')
# #    name:1240 => ('Hello')

# --------------------------------- example 2 -------------------------------- #
# def greet(msg, name, age=100):
#   print(f"{msg} {name}. You are {age} years old!")


# greet('Hello','Maria', 23)
# greet('Hello','Maria')

# --------------------------------- example 3 -------------------------------- #
# def greet(msg, name, age=100):
#   print(f"{msg} {name}. You are {age} years old!")


# greet('Hello','Maria', 23)
# greet(name='Maria', msg='Hello')


# --------------------------------- example 4 -------------------------------- #
# def add(x,y=9,*args):
  # x = 4
  # y = 5
  # args = ()
  # print(x,y,args)
  # print( args[-1] )
  # sum = 0
  # for el in args:
  #   sum+=el

  # print(sum(args))


# # add( (2,) )
# # add( (4,5) )
# # add( (2,3,4) )
# # add( (2,3,4,9,48) )

# add( 2 )
# add( 4,5 )
# add( 2,3,4 )
# add( 2,3,4,9,48 )

# ------------------------------ example kwargs ------------------------------ #
# def foo(**kwargs):
#   print(kwargs)
#   # TASK: print sum of kwargs values
#   print(kwargs['b'])


# foo( a=2,b=3,c=4 )
# foo( a=2,b=3 )
# foo( b=3,a=2 )


# ----------------------------- example unpacking ---------------------------- #

# def foo(a,b,c):
#   print(a)
#   print(b)
#   print(c)

# data = [1,2,3]
# # foo( data[0],data[1], data[2] )
# foo( *data)


# ----------------------- example unpacking dictionary ----------------------- #

# def foo(a,b,c):
#   print(a)
#   print(b)
#   print(c)

# data = {
#   'c':1,
#   'b':2,
#   'a':3
# }
# # foo( data['x'], data['y'], data['z'] )
# # foo( c=data['x'], b=data['y'], a=data['z'] )
# foo( **data)


