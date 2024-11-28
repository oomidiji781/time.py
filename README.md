# time.py
The code calculates the time when an alarm will go off after a certain number of hours, based on the current time.
# Input the current time and the number of hours to wait
str_time = input("What time is it now (0-23)? ")
str_wait_time = input("What is the number of hours to wait? ")

# Convert inputs to integers
time = int(str_time)
wait_time = int(str_wait_time)

# Validate input to make sure the time is between 0 and 23
if time < 0 or time > 23:
    print("Invalid time. Please enter a time between 0 and 23.")
else:
    # Calculate the time when the alarm will go off
    time_when_alarm_go_off = (time + wait_time) % 24

    # Format the result to show time as HH:00 (or HH if no minutes)
    print(f"The alarm will go off at {time_when_alarm_go_off:02}:00.")

