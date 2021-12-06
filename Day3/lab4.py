num=int(input("Enter an integer:"))
num1=int(input("Enter another integer"))
num2=int(input("Enter another integer"))

if num<num1 and num<num2:
    print(f"The {num} is smallest one.")
elif num1<num and num1<num2:
     print(f"The {num1} is smallest one.")
else:
    print(f"The {num2} is smallest one.")
        

