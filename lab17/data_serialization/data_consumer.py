# ---------------------------- parse data by hand ---------------------------- #
# with open('./data/data.txt') as f:
# 	content = f.read()

# data = map(int,content.split('|'))

# print(sum(data))


# --------------------------- parse data by pickle --------------------------- #
# import pickle

# data = pickle.load(open('./data/data.pickle','rb'))
# print(data)

# ------------------------------- parse by json ------------------------------ #
import json

with open('./data/data.json') as f:
	data = json.load(f)

for user in data:
	print(user)