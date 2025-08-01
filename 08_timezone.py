import pytz # command dite hobe ----> pip instll pytz ---ekbar install korle ar istall korte hoy na file e add hoye jay .venv(virtual environment) likha ache dekhoand pycache
import datetime
import time

# ঢাকার টাইমজোন
dhaka = pytz.timezone('Asia/Dhaka')

# বর্তমান UTC সময়
utc_now = datetime.datetime.now(pytz.UTC)

# UTC থেকে ঢাকার টাইমে কনভার্ট
dhaka_time = utc_now.astimezone(dhaka)

print("UTC Time:", utc_now)
print("Dhaka Time:", dhaka_time)



# ------------------------------
# print(pytz.all_timezones)
# ----------------------------------------------

start = datetime.datetime.now()
time.sleep(5) # 5 sec er jonno code execution pause kore rakhe 

# 5 sec por below code gulo run korbe 

end = datetime.datetime.now()

print("Duration:", end - start) 

# ------------------------------------------------
