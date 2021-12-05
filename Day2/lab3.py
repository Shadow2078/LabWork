#adding seconds in MidNight
Min=int(input("Enter Minutes"))
a=12
b=00
c=Min//(60)
d=float(Min%(60))
a=a+c
b=b+d
print(f"After given minutes, the time will be: {a} {b}")