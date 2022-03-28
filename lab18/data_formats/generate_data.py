

# --------------------------------- with CSV -------------------------------- #
import csv

data = [
	{
		'apple':2.50,
		'bananas': 3.50,
		'strawberries': [1,2,3]
	},
	{
		'apple':4.50,
		'bananas': 1.50,
		'strawberries': [2,1,3]
	},
]

output_file = 'data.csv'

with open(output_file,'w') as f:
	writer = csv.writer(f)

