from datetime import datetime, timedelta

today = datetime.today().date() #.date add korle sudhu date ashbe
tomorrow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)

print(today)
print(tomorrow)
print(yesterday)
# -----------------
now = datetime.today()
new_time = now + timedelta(hours =5, minutes=30) #extra time add hobe
print(now)
print(new_time)

# -----------------------
date1 = datetime(2025, 12, 25)
date2 = datetime(2025, 12, 5)

print(date1 - date2)

# ------------------timezone utc -------
#etar jonno ekta package proyojon hoy (pytz) next file e korbo timezone niye kaj 

