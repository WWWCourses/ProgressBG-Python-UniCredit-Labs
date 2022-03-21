import os

# cwd = os.getcwd()
# print(cwd)

# files = os.listdir(cwd)
# print(files)

# ------------------------------ Make directory ------------------------------ #

# # os.mkdir('./test/music')
# os.makedirs('./A/B')
# print(os.listdir('./test'))

# os.chdir('./test')

# os.makedirs('./A/B')

# print(os.listdir())

# ---------------------------- working with files ---------------------------- #
os.chdir('./test')
# fh = open('./sample.txt', mode="r")

# # content = fh.read()
# # print(content)
# print(fh.readlines())

# fh = open('./sample.txt', mode="a")
# # fh.write('\nThis is a new line')

# new_linews = ['line1\n', 'line2\n', 'line3\n']
# fh.writelines(new_linews)

# fh.close()

# with open('./sample.txt', mode="a") as fh:
# 	fh.write('\nThis is a new line')


file_path = './sample.txt'
stat = os.stat(file_path)
print(stat)
