odd=[]
even=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
        # print(len(even))
    else:
        odd.append(i)
        # print(len(odd))
print(len(even))
print(len(odd))


#Another Way
a=int(input("Enter a number:"))
j=0
k=0
for i in range(1,a+1):
    if i%2==0:
        j=j+1
    else:
        k=k+1
print("Number of even number:{}".format(j))
print("Number of odd numbers:{}".format(k))
      