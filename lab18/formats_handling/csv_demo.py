import csv

filename = './data.csv'
# with open(filename,'r') as f:
# 	data = csv.reader(f)
# 	header = next(data)

# 	for row in data:
# 		print(row)

with open(filename,'r') as f:
	data = csv.DictReader(f)
	for el in data:
		print(el)