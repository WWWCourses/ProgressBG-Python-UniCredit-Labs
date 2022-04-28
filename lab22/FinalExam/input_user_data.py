import json

def input_user_data():
	"""
	This function asks the user for input and returns a dictionary with the user's data.
	"""
	user_data = {}
	user_data["name"] = input("Enter user name:")
	user_data["age"] = input("Enter user age: ")
	user_data["city"] = input("Enter user city: ")
	return user_data

def print_users_data(users):
	"""
	This function prints the users' data.
	"""
	for user in users:
		print(f"Name: {user['name']}")
		print(f"Age: {user['age']}")
		print(f"City: {user['city']}")
		print()

def save_users_data(users, filename):
	"""
	This function saves the users' data in a json file.
	"""
	with open(filename, 'w') as file:
		json.dump(users, file)


# users = [
# 	{"name": "Pier", "age": "40", "city": "Paris"},
# 	{"name": "John", "age": "25", "city": "New York"},
# 	{"name": "Sara", "age": "45", "city": "London"},
# 	{"name": "Mary", "age": "30", "city": "Paris"},
# 	{"name": "Bob", "age": "35", "city": "London"},
# 	{"name": "Mike", "age": "50", "city": "London"},
# ]

# print_users_data(users)
# save_users_data(users, "users.json")

users = list()
while True:
	answ = input("Enter new user data [y/n]?: ")
	if answ == "y":
		user_data = input_user_data()
		users.append(user_data)
	else:
		print_users_data(users)
		save_users_data(users, "users.json")
		print('Goodbye!')
		break

