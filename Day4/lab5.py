print("To know whether you can enter or not in classes:")
print("Enter the number of classes held:")
tc=int(input())
print("Enter the number of classes attended:")
ac=int(input())
percentage=(ac/tc)*100
if percentage>75:
    print("You are allowed to enter the class.")
else:
    print("Get Out ! You are not allowed to enter the class.")
