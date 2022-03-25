import datetime as dt


def calc_remaing_days(user_birth_date):
	time_diff=user_birth_date-today
	return time_diff.days

today=dt.datetime.today().date()

user_birth_date=input('enter birthdate in format DD.MM.YYYY: ')
user_birth_date=dt.datetime.strptime(user_birth_date, '%d.%m.%Y').date()

# td = today - user_birth_date

# print( user_birth_date + (current_year-user_birth_year))

# print(user_birth_day,user_birth_month)

# days = calc_remaing_days(user_birth_date)
# print(days)

# 01.01.2000

# 25.03.2022


