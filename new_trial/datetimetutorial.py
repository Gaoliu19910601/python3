
import datetime
import pytz
import builtins

tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)

print(tday)
print(tday.weekday())
print(tday + tdelta)

bday = datetime.date(2017,11,27)

till_bday = bday - tday

print(till_bday)

t = datetime.time(9,15,15,100)

print(t)

total_t = datetime.datetime(2017,10,9,6,45,45)

print(total_t)

tdelta2 = datetime.timedelta(hours=72)

total_t2 = tdelta2 + total_t

print(total_t2)

dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_now)

dt = datetime.datetime(2017,10,10,12,30,45,tzinfo=pytz.UTC)

print(dt)

dt_now_pytz = datetime.datetime.now(tz=pytz.UTC)

print(dt_now_pytz)

# for tz in pytz.all_timezones:
    # print(tz)

# print(dir(builtins))

li = [5,4,6,3,8,2,7,9,1]

li.sort(reverse=True)

print(li)