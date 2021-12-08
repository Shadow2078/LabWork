'''Find the absolute value of number
'''
print("Enter a number:")
num=int(input())
x=-1
if num>0:
    print(num)
else:
    print("The absolute value is:",num*x)

    #Using for loop

print("Absolute value using for loop:",end=" ")
for i in str(num):
    if i=="-":
        continue
    print(i,end=" ")
print(" ")

    #Using while loop
print("Absolute value using while loop:",end=" ")
j=0
while j<len(str(num)):
    if str(num)[j]=="-":
        j+=1
        continue
    else:
        print(str(num)[j],end="")
        j+=1