#Datetime

import datetime

mytime = datetime.time(2,20)

print(mytime.minute)
# 20
print(mytime.hour)
# 2
print(mytime)
#02:20:00

today = datetime.date.today()

print(today)
# 2022-01-25

print(today.year)
#2022

print(today.month)
#1

print(today.ctime())
#Tue Jan 25 00:00:00 2022

from datetime import datetime

mydatetime = datetime(2021,10,3,14,20,1)

print(mydatetime)
#2021-10-03 14:20:01

mydatetime = mydatetime.replace(year=2020)

print(mydatetime)
#2020-10-03 14:20:01

from datetime import date

date1 = date(2021,11,3)

date2 = date(2020,11,3)

print(date1 - date2)
#365 days, 0:00:00

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

print(datetime1 - datetime2)
#365 days, 10:00:00