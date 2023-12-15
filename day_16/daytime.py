# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()

current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
timestamp = now.timestamp()

print(f"Current Day: {current_day}")
print(f"Current Month: {current_month}")
print(f"Current Year: {current_year}")
print(f"Current Hour: {current_hour}")
print(f"Current Minute: {current_minute}")
print(f"Timestamp: {timestamp}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
converted_time = datetime.strptime(time_string, "%d %B, %Y")
print(f"Converted Time: {converted_time}")

# Calculate the time difference between now and new year.
from datetime import timedelta

new_year = datetime(now.year + 1, 1, 1)
time_difference_to_new_year = new_year - now

print(f"Time difference to New Year: {time_difference_to_new_year}")

# Calculate the time difference between 1 January 1970 and now.
epoch_time = datetime(1970, 1, 1)
time_difference_to_epoch = now - epoch_time

print(f"Time difference to 1 January 1970: {time_difference_to_epoch}")

# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog