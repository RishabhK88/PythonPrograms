from datetime import datetime, timedelta
# time delta represents duration
dt1 = datetime(2018, 1, 1) + timedelta(days=1)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("Days:", duration.days)
print("Seconds:", duration.seconds)
print("total_seconds", duration.total_seconds())
