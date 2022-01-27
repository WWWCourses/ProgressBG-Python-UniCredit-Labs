

name = ['Maria', 'Ivan', 'Asen']
number = ['+39587111111', '+39587222222', '+39587333333']
bills = [20.5, 30.48, 5.98]

users = list(zip(name, number))
users_data_1 = dict(enumerate(users, 1))

print(users_data_1)


users_data_2 = {
    1: ['Maria', '+35987111111'],
    2: ['Ivan', '+35987222222'],
    3: ['Asen', '+35987333333']
}



id = 4
name = 'Pesho'
tel = '+1111111'

users_data_1[id]= (name,tel)
print(users_data_1)


users_data_2[id]= [name,tel]
print(users_data_2)


