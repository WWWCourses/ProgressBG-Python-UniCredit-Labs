# -------- TASK: filter list of numbers to contain only even numbers: -------- #
# Solutions with for loop:
# numbers = [1,2,3,4,5]
# even_numbers = []

# for el in numbers:
# 	if el%2==0:
# 		even_numbers.append(el)

# Solutions with list comrehension:
# numbers = [1,2,3,4,5]
# even_numbers = [el for el in numbers if el%2==0]

# print(even_numbers)
# # [2,4]

# Solutions with filter:
# numbers = [1,2,3,4,5]

# def is_even(x):
# 	return True if x%2==0 else False

# even_numbers = filter(is_even, numbers)
# print( list(even_numbers) )

# numbers = [1,2,3,4,5]
# even_numbers = filter(lambda x: True if x%2==0 else False, numbers)
# print( list(even_numbers) )


# --------------- TASK: Map each element of numbers into el**2 --------------- #
# numbers = [1,2,3,4]

# Solution with list comprehension
# powered = [ el**2 for el in numbers]

# print( powered )
#  [1,4,9,16]

# Solution with map
# powered = map(lambda el:el**2, numbers)
# print( list(powered) )


# ---------------------------- map multiple lists ---------------------------- #
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = [3,4,5,6]

# paralel_sums = map( lambda x,y,z: x+y+z, l1, l2,l3)

# print(list(paralel_sums))


# ------------------ TASK: reduce list of numbers to its sum ----------------- #
# from functools import reduce

# numbers = [1,2,3,4]
# sum = reduce(lambda x,y: x+y, numbers, 0)
# print(sum)


# ------------- TASK: map list of dictionaris to list of numbers ------------- #
# products = [
# 	{'name':'apples', 'price': 2},
# 	{'name':'oranges', 'price': 5},
# 	{'name':'bananas', 'price': 3},
# ]

# prices = map(lambda x:x['price'], products)
# print( list(prices) )
# # prices = [2,5,3]


# ------------- TASK: reduce list of dictionaris to sum of prices ------------- #
# from functools import reduce

# products = [
# 	{'name':'apples', 'price': 2},
# 	{'name':'oranges', 'price': 5},
# 	{'name':'bananas', 'price': 3},
# ]

# sum = reduce(lambda x,y:x+y['price'], products, 0)
# print(sum)

# def foo(*t):
# 	print(t)

# foo(1,2,3)