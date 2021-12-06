English=int(input("Enter your marks of English:"))
Math=int(input("Enter your marks of Math:"))
Science=int(input("Enter your marks of Science:"))
Health=int(input("Enter your marks of Health:"))
Social=int(input("Enter your marks of Social:"))

Total=English+Math+Science+Health+Social


percentage=(Total/500)*100

print(f"Your percentage is:{percentage} %")
if percentage>70 and percentage <=100:
    print("Distinction")
elif percentage>60 and percentage <=70:
    print("First Division")
elif percentage>40 and percentage<= 60:
    print("Passed")
elif percentage<=40:
    print("Failed")



