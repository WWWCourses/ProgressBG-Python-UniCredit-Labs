# import time
# print(int(time.time()))


# import datetime, pytz

# unaware = datetime.datetime(2018, 11, 21, 9, 12, 32, 0)

# aware = datetime.datetime(2018, 11, 21, 9, 12, 32, 0, pytz.timezone('US/Eastern'))
# aware2 = datetime.datetime(2018, 11, 21, 9, 12, 32, 0, tzinfo=pytz.timezone('Europe/Amsterdam'))


# print(unaware)
# print(aware)
# print(aware2)

# ------------------------------- datetime.time ------------------------------ #
from calendar import weekday
import datetime as dt

# lunch_time = dt.time(hour=12, minute=0, second=0)
# print(lunch_time)
# print(lunch_time.minute)

# # get current datetime
# now = dt.datetime.now()
# today = dt.datetime.today()

# print(now.year)
# print(today)


# now = dt.datetime.now()

# formated datetimes
# get the date object
# today = dt.datetime.today()
# today_formated = today.strftime("%d.%m.%Y-%H:%M:%S")
# print(today_formated)

# birth_day_str = "31.01.2000" #'%d.%m.%Y'

# birth_day = dt.datetime.strptime(birth_day_str, "%d.%m.%Y")
# print(birth_day)


# utcnow = dt.datetime.utcnow()
# print(utcnow)


# --------------------------------- examples --------------------------------- #
today = dt.datetime.today()
weekdays = ["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"]
print( weekdays[today.weekday()] )