import datetime
import pytz

def show_time_for_timezone():
    print("Timezone Converter (Type 'exit' to quit)")
    print("Example timezones: Asia/Dhaka, America/New_York, Europe/London, Asia/Tokyo")
    
    while True:
        zone_input = input("\nEnter a timezone: ")

        if zone_input.lower() == "exit":
            print("Exiting Timezone Converter.")
            break
        
        if zone_input not in pytz.all_timezones:
            print("Invalid timezone! Try again.")
            continue
        
        timezone = pytz.timezone(zone_input)
        current_time = datetime.datetime.now(pytz.UTC).astimezone(timezone)
        print(f"Current time in {zone_input}: {current_time.strftime('%Y-%m-%d %I:%M:%S %p')}")

# Run the tool
show_time_for_timezone()
