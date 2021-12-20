# print program menu:
print("Select an action:")
print("1. Action 1")
print("2. Action 3")
print("3. Action 3")

while True:
	user_choice = int(input("Enter a number [1-3]: "))

	if user_choice not in {1,2,3}:
		print('invalid action')
		# break
		continue


	# do this only if user_choice = 1, 2,3
	if user_choice == 1:
		print("Action 1 fired!")
		break
	elif user_choice == 2:
		print("Action 2 fired!")
		break
	elif user_choice == 3:
		print("Action 3 fired!")
		break
	else:
		pass
