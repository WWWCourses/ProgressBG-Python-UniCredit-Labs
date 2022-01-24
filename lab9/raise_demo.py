# print(1)
# raise
# print(2)

# try:
# 	user_number = int(input("Enter a number: "))
# except:
# 	print('Log error')
# 	raise

# --------------------------- custom error rainsing -------------------------- #
# define custom exception
class UserNameError(Exception):
	pass

try:
	user_name = input("Enter your name: ")
	if len(user_name)<3:
		raise UserNameError
except UserNameError:
	print("User name must be at least 3 symbols long")
except:
	print('Oops! Something went wrong!')