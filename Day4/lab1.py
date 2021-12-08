'''Check whether the given year is a leap year or not. If year is leap print "Leap Year" otherwise print "Commmon Year".
Hint: a year is a leap  year if its number is exactly divisible by 4 and is not exactly divisible by 100. 
A year is always a leap year if its number is exactly divisible by 400.'''
year=int(input("Enter a year:"))
if year%4==0 and year%100!=0:
    print("It's a leap year.")
else:
    print("No,It's a Common Year.")
year1=int(input("Enter another year:"))
if year%400==0:
    print("It is also a leap year.")
else:
    print("It is not leap year.")