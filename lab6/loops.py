# -------------------------------- while loop -------------------------------- #
# x = 0
# while x<5 :
# 	print('hi', x)
# 	x=x+1

# for x in range(5):
# 	print('hi', x)

# print('END')


# i = 1
# sum = 0

# while i <= 100:
# 	if i%2==0:
# 		sum += i
# 	i += 1

# print("sum = ", sum)

# --------------------------------- for loop --------------------------------- #
# for item in [1,2,3,4,5]:
# 	print(item)
# print('END')


# m = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# ]

# for row in m:
# 	# print(row)
# 	for el in row:
# 		print(el**2)


# ------------------------------ break statement ----------------------------- #

x = 1
while x>0:
	print(x)
	x=x+1

	if x>5:
		break

	print('HI')



# ------------------------------ do - while demo ----------------------------- #
### Python doesn't have do - while, so in next demo we copy-paste the block,
### as we want the block to be executed at-least one:

# user_name = input("Enter a name (at least 3 symbols): ")
# user_name_length = len(user_name)

# while (user_name_length<3):
# 	user_name = input("Enter a name (at least 3 symbols): ")
# 	user_name_length = len(user_name)

### but copy-paste is BAD Practice, so it's betters to:
while True:
	user_name = input("Enter a name (at least 3 symbols): ")
	user_name_length = len(user_name)

	if user_name_length > 3:
		break

# print("Thank you, {}!".format(user_name))