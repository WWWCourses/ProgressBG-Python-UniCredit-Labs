# TASK: print line by line the content of 'test.txt'
import os

# # set CWD to 'file_operatio'
script_path = os.path.dirname(__file__)
print(f'script_path: {script_path}')
print(f'CWD: {os.getcwd()}')

os.chdir(script_path)

# with open(script_path+'data/test.txt','r') as f:
with open(os.path.join(script_path,'data/test.txt'),'r') as f:
	# read from f
	for line in f.readlines():
		print(line.strip())



# line1
# line2
# line3