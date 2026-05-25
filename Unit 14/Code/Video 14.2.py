# Date

# from datetime import date
# d = date(2026, 2, 10)
# print(d)
# print(d.day)
# print(d.month)
# print(d.year)
# print(date.today())

# Time

# from datetime import time
# t = time(14, 30, 15)
# print(t)
# print(t.hour, t.minute, t.second)


# datetime

# from datetime import datetime
# dt = datetime(2026, 2, 10, 14, 30, 15)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(datetime.now())

# timedelta

# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# print(now + timedelta(days=7))
# print(now - timedelta(hours=2))


# formatting dates/times

# from datetime import datetime, timedelta
# dt = datetime.now()
# print(dt.strftime("%Y-%m-%d"))
# print(dt.strftime("%d/%m/%Y"))
# print(dt.strftime("%I:%M %p"))
# print(dt.strftime("%A, %B %d, %Y"))


# parsing string to datetime

# from datetime import datetime, timedelta
# s = "10-02-2026 14:30:15"
# dt = datetime.strptime(s, "%d-%m-%Y %H:%M:%S")
# print(dt)


# Common Operations

# combine

# from datetime import date, time, datetime
# dt = datetime.combine(date(2026, 2, 10), time(9, 15))
# print(dt)

# replace

# from datetime import datetime
# dt = datetime(2026, 2, 10, 9, 15)
# print(dt.replace(hour=10, minute=5))


# comparison

# from datetime import date
# print(date(2026, 2, 10) > date(2026, 2, 1))














