from copyreg import pickle


data = {
	'apple':2.50,
	'bananas': 3.50,
	'strawberries': []
}

# ---------------- serialize by hand  - the worst possible way --------------- #
# output_file = 'data.txt'
# serialized_data =''

# for k,v in data.items():
# 	# print(k,v)
# 	serialized_data+=f'{k}:{v}\n'

# with open(output_file, 'w') as f:
# 	f.write(serialized_data)


# --------------------------- serialize with pickle -------------------------- #
# import pickle

# output_file = 'data.pckl'

# # serialized_data = pickle.dumps(data)

# # with open(output_file, 'wb') as f:
# # 	f.write(serialized_data)

# pickle.dump(data, open(output_file,'w'))

#

# --------------------------------- with JSON -------------------------------- #
# import json

# output_file = 'data.json'
# print( json.dumps(data) )

# json.dump(data, open(output_file,'w'))

