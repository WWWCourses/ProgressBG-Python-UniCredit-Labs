# --------------------------------- with CSV -------------------------------- #
from contextlib import redirect_stderr
import csv


data = dict()
with open('./demo.csv','r') as f:
	# reader = csv.reader(f)
	reader = csv.DictReader(f)

	print(reader)

	for k in reader:
		print(k)

	# skip header line
	# reader.__next__()
	# next(reader)

	# for l in reader:
	# 	data.append(l)

