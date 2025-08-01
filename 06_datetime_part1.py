import datetime

now = datetime.datetime.now()
print(now)
# --------------
today_date = datetime.date.today()
print(today_date)

# -------------------
today_time = datetime.datetime.now().time()
print(today_time)


# -----
custom_datetime = datetime.datetime(2040,2,23,10,30,0)
print(custom_datetime)

# -----
formate_datetime = now.strftime("%Y/%m/%d %H:%M:%S")
print(formate_datetime)

# -------------
formate_datetime = now.strftime("%Y/%B/%d %H:%M:%S") #B use korle month er english name ashbe

print(formate_datetime)

# -----------
formate_datetime = now.strftime("%Y/%b/%d %H:%M:%S") #small b use korle month er name er first 3 word ashbe.

print(formate_datetime)

# -----
formate_datetime = now.strftime("%Y/%b/%d %A%H:%M:%S") # A use korle week er name ashbe and small a use korle week er name er first 3 word ashbe.

print(formate_datetime)

# ---------------
formate_datetime = now.strftime("%Y/%b/%d %A%H:%M:%S %p") #  am pm er jonno %p 
print(formate_datetime)

# --------
date_str = "25-12-2030 10:45:00"
parsed_date = datetime.datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")
print(parsed_date)
print(type(parsed_date))