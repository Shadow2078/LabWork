# convert 86400 seconds to day, hours, minutes, seconds
sec=int(input("Enter Seconds"))
day=sec/(60*60*24)
Hrs=sec/(60*60)
Min=sec/60
print(f"86400 seconds equal to {day}day and {Hrs}hours and {Min}minutes")