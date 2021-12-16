word=input("Enter a word:")
i=0
j=0
for k in word:
    if k.isdigit():
        i=i+1
    elif k.isalpha():
        j=j+1
    else:
        pass
print("Letters",j)
print("Digits",i)

'''Write a Python program that accepts a string and calculate
 the number of digits and letters  '''
    