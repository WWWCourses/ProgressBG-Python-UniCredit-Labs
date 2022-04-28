import json

def read_user_data(filename):
	"""
	This function reads the users' data from a json file.
	"""
	with open(filename, 'r') as file:
		users = json.load(file)
	return users

def print_users_data(msg, users):
	"""
	This function prints the users' data.
	"""
	print(msg)
	for user in users:
		print("\tUser name:", user["name"])
		print("\tUser age:", user["age"])
		print("\tUser city:", user["city"])
		print()

def calculate_average_age(users):
	"""
	This function calculates the average age of the users.
	"""
	total_age = 0
	for user in users:
		total_age += int(user["age"])
	average_age = total_age / len(users)
	return average_age

def find_users_by_city(users, city):
	"""
	This function finds the users by city.
	"""

	# found_users = []
	# for user in users:
	# 	if user["city"] == city:
	# 		found_users.append(user)
	# return found_users

	return [user for user in users if user["city"] == city]

def sort_users_by_name(users):
	"""
	This function sorts the users by name.
	"""

	return sorted(users, key=lambda user: user["name"])

def show_main_menu():
	print()
	print("""1. Print all users
2. Print average users age
3. Find users by city
4. Sort users by name
5. Quit""")
	print('*' * 30)



if __name__ == "__main__":
	users = read_user_data("users.json")
	show_main_menu()

	while True:
		answ = input("Enter your choice: ")
		if answ == "1":
			print_users_data('All users:', users)
			show_main_menu()
		elif answ == "2":
			print("Average age:", calculate_average_age(users))
			print()
			show_main_menu()
		elif answ == "3":
			cities = list(set([user["city"] for user in users]))
			print("Cities:", cities)
			city = input("Enter city: ")
			found_users = find_users_by_city(users, city)
			print_users_data(f'Users from {city}:',found_users)
			show_main_menu()
		elif answ == "4":
			sorted_users = sort_users_by_name(users)
			print_users_data('Users sorted by name: ',sorted_users)
			show_main_menu()
		elif answ == "5":
			print("Goodbye!")
			break
		else:
			print("Invalid choice!")
			continue
