# i = 1

# while i<=5:
# 	print(i)
# 	i+=1

# for i in range(1,6):
# 	print(i)


# TASK: user must enter password >=5 symbols
# password = input('enter a password (at least 5 symbols):')

# while len(password)<5:
# 	password = input('enter a password (at least 5 symbols):')


# do {
# 	password = input('enter a password (at least 5 symbols):')
# } while len(password)<5

while True:
	password = input('enter a password (at least 5 symbols):')
	if len(password)>=5:
		break
