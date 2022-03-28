# ---------------- de-serialize by hand  - the worst possible way --------------- #
# input_file = 'data.txt'

# data = {}
# with open(input_file) as f:
# 	for line in f:
# 		line = line.rstrip()
# 		# print(line)
# 		key, value = line.split(':')
# 		data[key] = value


# print(data)
# apple:2.50\n
# bananas: 3.50\n
# strawberries: 5.5\n


# --------------------------- de-serialize with pickle -------------------------- #
# import pickle

# input_file = 'data.pckl'

# data = pickle.load( open(input_file, 'r') )

# print(data)

# --------------------------------- with JSON -------------------------------- #
import json

input_file = 'data.json'

data = json.load( open(input_file, 'r') )

for el in data:
	print(el['apple'])

