clients = {  (1,2,3), ("Maria", "Ivan", "Asen"), ("+39587111111", "+39587222222", "+39587333333") }
bills = { (1,2,3), (25.50, 30.48, 5.98) }

clients_bills = clients.union(bills)

# print(clients_bills)


for item in clients_bills:
	print(item)