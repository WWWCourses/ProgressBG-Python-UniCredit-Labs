import os

# get files in data
files = os.listdir('./data')
print(files)


for file in files:
	with open(os.path.join('./data',file),'r') as f:
		print(f.readlines())
