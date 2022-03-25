import os
# ------------------------------ read from file ------------------------------ #
# file_path = 'test.txt'

# fh = open(file_path, mode='r')

# read the whole content into string var.
# content = fh.read()
# print(content)

# read first 10 characters:
# content = fh.read(10)
# print(content)

# read and do something with each line:
# print( fh.readline(), end='' )
# print( fh.readline(), end='' )
# print( fh.readline(), end='' )

# # for line in fh.readlines():
# # for line in list(fh):
# for line in fh:
# 	line = line.rstrip()
# 	print(f'>{line}<')

# fh.close()

# ------------------------------- write in file ------------------------------ #
# file_path = 'test.txt'

# # open for write and truncate:
# fh = open(file_path, mode='w')

# data_str = '''
# line A
# line B
# '''

# fh.write(data_str)

# data_list = ['lineA', 'lineB']
# fh.writelines(data_list)

# fh.write(data_str)


# -------------------------------- remove file ------------------------------- #
# os.remove('test.txt')


# --------------------------- with context manager: -------------------------- #
# do not use that:
# try:
# 	fh = open('test.txt', mode='r')
# 	content = fh.read()
# except:
# 	print(f'File did not exists')
# finally:
# 	fh.close()


# with open('test.txt', mode='r') as fh :
# 	content = fh.read()
# 	print(content)

# print('File is closed')


# os.rename('src/test.txt','dest/test.txt_9432932' )

# print(os.listdir('src'))


