# Error, not Exception
# x = 'abc"

# Exception
# print(x)
# x = 1/0

try:
	user_number = int(input("Enter a number: "))
	res = 10/user_number
except ValueError:
	print("You did not enter a number!")
	exit(1)
except ZeroDivisionError:
	print("Enter a number different from zero (0)!")
	exit(1)
except:
	print('Oops, something went woring ')

print('Program continues....')



# 'a'
