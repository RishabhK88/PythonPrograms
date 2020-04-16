from datetime import datetime
import time

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()  # gives current time
# for converting datetime string into datetime objects
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
# we can find directives for strptime in python documentation

# converting timestamp to datetime object
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
dt = dt.strftime("%Y/%m")  # covert datetime object to string
print(dt)

print(dt2 > dt1)  # comparing dates
