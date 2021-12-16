'''
Given a n digit number. Find the sum of its digits.
'''
number=int(input("Enter a number"))
sumofdigits=0
for digit in str(number):
    sumofdigits=sumofdigits+int(digit)
print(sumofdigits)