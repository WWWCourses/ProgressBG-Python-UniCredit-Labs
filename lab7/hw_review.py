bills = {1: 25.5, 2:30.48, 3: 5.98}
# clients_names = ['Maria', 'Ivan', 'Asen']
clients_names = [
	{
		id: 1,
		name:'Maria',
		tel:083928493893
	}
]

max_bills_dict = { bills_key: bills_value for bills_key, bills_value in list(bills.items()) if bills_value == max(bills.values())}

for key, value in max_bills_dict.items():
	print(key,value)
	# max_key = ("{}".format(key))
	max_key = f"{key}"
	max_bill =  ("{}".format(value))

# print(f'The user with highest bill - {max_bill} is {clients_names[int(max_key)]}')

min_bills_dict = { bills_key: bills_value for bills_key, bills_value in list(bills.items()) if bills_value == min(bills.values())}

for key, value in min_bills_dict.items():
	min_key = ("{}".format(key))
	min_bill =  ("{}".format(value))

# print(f'The user with lowest bill - {min_bill} is {clients_names[int(min_key)]}')