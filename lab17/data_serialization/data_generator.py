# generate somehow data:
from copyreg import pickle

# data = [1,2,3]
# output_file = './data/data.txt'

# # ---------------------------- serialize 'by hand' --------------------------- #
# # serialize and save
# with open(output_file,'w') as f:
# 	data_str = '|'.join(map(str,data))
# 	f.write(data_str)

# --------------------------- serialize with pickle -------------------------- #
# import pickle

# data = [
# 	{'name':'Ada','balance':1000}
# ]


# output_file = './data/data.pickle'
# # zed = pickle.dumps(data)
# pickledata_serali.dump(data,open(output_file,'wb'))

# ---------------------------- serialize with JSON --------------------------- #
import json
data = [
	{'name':'Ada','balance':1000, 'is_credit':True},
	{'name':'Pesho','balance':2.500, 'is_credit':False}
]

output_file = './data/data.json'
with open(output_file,'w') as f:
	json.dump(data, f, indent=4)
