import datetime
import calendar


now = datetime.datetime.today()

print(calendar.day_name[now.weekday()])

urodziny=datetime.datetime(1984,4,15)
print(calendar.day_name[urodziny.weekday()])


