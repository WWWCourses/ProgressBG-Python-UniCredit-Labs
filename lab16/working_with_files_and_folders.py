import os

script_folder = os.path.dirname(os.path.realpath(__file__))
# print(script_folder)

cwd  = os.getcwd()
# print(cwd)

os.chdir(script_folder)

# print(os.getcwd())

# print(os.listdir())

# ------------------------------ make directory ------------------------------ #
# os.mkdir('./test')
# os.makedirs('./A/B/C')

# ---------------------------------- rename ---------------------------------- #

# os.rename('./A/B/test.py', 'test2')

os.rmdir('../lab1/')

