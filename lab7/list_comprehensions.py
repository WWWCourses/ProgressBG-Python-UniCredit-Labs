# ---------------------------- list comprehensions --------------------------- #
# syntax:
# newlist = [expression for item in iterable if condition]

### example 1
## with for loop
# newlist = []
# for item in [1,2,3]:
# 	newlist.append(1+2)

## with list comprehension:
# newlist = [1+2 for item in [1,2,3] ]
# print(newlist)

### examle 2
# Create new list of numbers, from l, where element is divisible by 3

# l = [2,1,5,6,74]

## with for loop
# divisible_by_three = []
# for item in l:
# 	if item%3==0:
# 		divisible_by_three.append(item**2)

## with list comprehension:
# divisible_by_three = [ item**2 for item in l if item%3==0 ]
# print(divisible_by_three)

### example 3
# TASK: generate a new list from a given list l, where each even number is replaced with 1 and odd number - with 0.

l = [2,5,3,4,5]
## with for loop and if-else
# new_list = []
# for el in l:
# 	if el%2:
# 		# odd el
# 		new_list.append(0)
# 	else:
# 		# even el
# 		new_list.append(1)

## with for loop and ternary operator(value = val_1 if cond else val_2)
# for el in l:
# 	value = 0 if el%2 else 1
# 	new_list.append(value)

## with list comprehension and ternary operator:
# new_list = [0 if el%2 else 1 for el in l]
# print(new_list)
