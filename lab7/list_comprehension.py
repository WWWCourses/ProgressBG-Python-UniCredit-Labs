# ---------------------------- list comprehension ---------------------------- #
# newlist = [expression for item in iterable]
# newlist = [ el+1 for el in [1,2,3] ]
# print(newlist)

# for el in l:
# 	l_new.append(el+2)


### TASK: from l, create l_new, where each element of l is sqrt()
# with for loop
# l = [1,2,3,4,5]
# l_new = []

# for el in l:
# 	l_new.append(el**2)

# print(l_new)

# with list comprehension

# l = [1,2,3,4,5]
# l_new = [ el**2 for el in l ]
# print(l_new)

## full syntax:
# newlist = [expression for item in iterable if condition]

# newlist = []
# for item in iterable:
# 	if condition:
# 		newlist.appent(expression)

# l = [1,2,3,4,5]
# l_new = [ el+1 for el in l if el%2 ]

# print(l_new)
# [3,5]
# [2,4,6]


# ------------------------- dictionary comprehension ------------------------- #
# TASK:
# students_score = {
# 	'Ivan':   5.00,
# 	'Alex':   3.50,
# 	'Maria':  5.50,
# 	'Georgy': 5.00,
# }

## with for loop
# best_students_score = {}
# # best_students_score['Ivan'] = 5.00

# for key,value in students_score.items():
# 	if value>4.0:
# 		best_students_score[key] = value

# print(best_students_score)

## with comprehension
# best_students_score = {key:value for key,value in students_score.items() if  value>4.0 }
# print(best_students_score)
