# ---------------------------------- filter ---------------------------------- #
# def is_even(x):
# 	return True if x!=0 and x%2==0 else False


# # print( type(is_even) )
# # print( type(is_even(2)) )

# even_numbers = filter( is_even, [1,2,3,4,5,6,7])

# is_even(1) => True , 1 is appended to even_numbers
# is_even(2) => False, 2 is pass away

# # print( list(even_numbers) )


# even_numbers = filter( lambda x: True if x!=0 and x%2==0 else False, [1,2,3,4,5,6,7])
# print( list(even_numbers) )

### task: filter empty strings
# names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
# cleared_names = []

## Solution with for loop:
# for el in names:
# 	if el:
# 		cleared_names.append(el)
# 	else:
# 		pass

# print( cleared_names )

## Solution with for list comprehension:
# names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
# cleared_names = [el for el in names if el]
# print(cleared_names)

## Solution with for filter:
# names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
# cleared_names = filter( lambda el: True if el else False, names)
# # print(cleared_names)

# for el in cleared_names:
# 	print(el)


# ------------------------------------ map ----------------------------------- #
# numbers = [1,2,3,4,5]

# sqr_numbers = map(lambda x:x**2, numbers)

# print( list(sqr_numbers) )

# TASK:  Generate all uppercase cyrillic letters by their UTF codes

# print( list(range(1040, 1072)) )
# print( chr(1040) )
# print( chr(1071) )

# upper_cyrillic = [ chr(code) for code in range(1040, 1072)]
# print(upper_cyrillic)

# upper_cyrillic = map(lambda code: chr(code), range(1040, 1072))
# upper_cyrillic = map(chr, range(1040, 1072))
# print(list(upper_cyrillic))

# map on multiple iterables
l1 = [1,2,3]
l2 = [4,5,6]

# desired output: [5,7,9]

l = map(lambda el1,el2: el1+el2, l1,l2)
print(list(l))



# ---------------------------------- reduce ---------------------------------- #
# from functools import reduce

# reduce list of numbers to its sum:
# def reducer(x,y):
# 	print(x, y)
# 	return x+y

# sum = reduce( reducer, [1,2,3,4,5], 0)
# print(sum)

# reduce products to sum of prices
# products = [
# 	{'name':'apples', 'price': 2},
# 	{'name':'oranges', 'price': 5},
# 	{'name':'bananas', 'price': 3},
# ]

# sum = reduce(lambda x,y:x+y['price'], products, 0)
# print(sum)