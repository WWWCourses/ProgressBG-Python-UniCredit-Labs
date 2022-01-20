# try:
#   # code, which can raise an exception
#   user_number = int(input("Enter a number: "))
#   print(5/user_number)
# except ValueError as e:
#   # do something if an Exception was raised
#   print("ValueError")
# except ZeroDivisionError:
# 	print('ZeroDivisionError')
# except:
# 	print('General error')
# else:
#   # do something only if there was no Exception
#   print("else clause")
# finally:
#   # do something no matter if an Exception was raised or not
#   print("finally clause")

# print('main end')

# --------------------------------- example 2 -------------------------------- #
# def get_user_number():
#   user_number = int(input("Enter a number: "))
# #   return user_number


# try:
#   x = get_user_number()
#   print(f'x = {x}')
#   res = 10/x
#   print("Result is {}".format(res))
# except ValueError:
#   print("You did not enter a number!")
# except ZeroDivisionError:
#   print("Enter a number different from zero (0)!")
# except:
#   print("Oops! Something went wrong!")

# ------------------------------- raise example ------------------------------ #
# try:
#   user_number = int(input("Enter a number: "))
# except ValueError:
#   print("~"*30)
#   print("You did not enter a number!")
#   print("~"*30)
#   raise

# print('end')

# print('start')
# raise ValueError
# print('end')


# class UserNameError(Exception):
# 	def __init__(self):
# 		print('UserNameError')


# try:
# 	user_name = input("Enter your name: ")

# 	if user_name == "pesho":
# 		raise UserNameError
# except:
# 	print('Error')

# print('Welcome', user_name)

# ------------------------ using error object example ------------------------ #
# try:
#   user_number = int(input("Enter a number: "))
#   print(5/user_number)
# except ValueError as error:
# 	print("ValueError")
# 	raise
# except ZeroDivisionError:
# 	print('ZeroDivisionError')
# except:
# 	print('General error')

# print('end')

input('x=')