age=int(input("Enter your age.:"))
gender=input("Enter your Gender(i.e M or F):")
if gender=='F':
    print("You will work in urban areas.")
elif gender=="M" and age>=20 and age<=40:
    print("You may work in anywhere.")
elif gender=="M" and age>=40 and age<=60:
    print("You will work in urban areas only")
else:
    print("Error")