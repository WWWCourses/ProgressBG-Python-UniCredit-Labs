# users = [
# 	{'name':'Maria', 'balance': 2000},
# 	{'name':'Petar', 'balance': -189},
# 	{'name':'Ivan', 'balance': 3200},
# 	{'name':'Asen', 'balance': -2890},
# ]

# names = map(lambda user:user['name'], users)
# print(list(names))


# example:
# l = [1,2,3,4] => [2,4] => [4,16]

l = [1,2,3,4]
l1 = map(lambda el:el**2, filter(lambda el: el%2==0,l))
print(list(l1))
