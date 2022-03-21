# import time, datetime, pytz

# print( time.time())


# unaware = datetime.datetime(2018, 11, 21, 9, 12, 32, 0)
# aware = datetime.datetime(2018, 11, 21, 9, 12, 32, 0, pytz.UTC)

# print(unaware)
# print(aware)


import datetime as dt

# lunch_time = dt.time(hour=12, minute=0, second=0)
# print(lunch_time)

# due_date1 = dt.date(month=11 ,year=2018, day=21)
# due_date2 = dt.date(2018, 11,21)
# print(due_date1)
# print(due_date2)

# user_birth = dt.datetime(year=1990, month=11, day=21, hour=13)
# print(user_birth)

# print(dt.datetime.now())
# print(dt.datetime.today())

# today = dt.datetime.today()
# user_birth = dt.datetime(year=2000, month=2, day=18, hour=13)
# time_diff = today-user_birth
# print(time_diff.seconds)

# utcnow = dt.datetime.utcnow()
# print(utcnow)

# today = dt.datetime.today()
# print(today.hour)

# --------------------------------- examples --------------------------------- #
# today = dt.datetime.today()
# # print(today.year)
# print(today.strftime('%d.%m.%Y (%B) %H:%M')) # 21.03.2022

# ---------------------------- task: calc user age --------------------------- #
# user_birth_str = '2000-02-18'
# user_birth = dt.datetime.strptime(user_birth_str, '%Y-%m-%d')
# today = dt.datetime.today()

# print(f'You are {today.year - user_birth.year} years old')

# from functools import reduce
# import time

# start = time.time()

# sum = reduce(lambda x,y:x+y, range(1,1_000_001))
# print("The sum of numbers from 1 to 1_000_000 is: ", sum)

# end = time.time()

# print( f'Time: {end-start}')

# ---------------------------- get week day in bg ---------------------------- #
# import datetime as dt

# named_wd = {
# 	'bg':["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
# 	'en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# }

# today = dt.datetime.today()
# week_num = today.weekday()

# day_name_bg = named_wd['bg'][week_num]
# print(day_name_bg)

# --------------------------- get_next_sunday_date --------------------------- #
import datetime

def get_next_sunday_date(bdate, period):
	years = []

	for y in range(*period):
		bdate_weekday = datetime.date(y, bdate.month, bdate.day).weekday()

		if bdate_weekday == 6:
			years.append(y)

	return years


birth_date = datetime.datetime.strptime("31/12/00", "%d/%m/%y")

sundays_years = get_next_sunday_date(birth_date, (2022,2100))
print(sundays_years)