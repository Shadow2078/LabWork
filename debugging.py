import pdb
bike1="yamaha"
bike_1=25000

bike2="honda"
bike2_price=50000

pdb.set_trace()
name=input("Enter you name :")
choose=int(input("press 1 for yamaha and 2 for honda:"))
print(f"hello{name}")
 
if choose==1:
    print("f{bike1} will cost you {bike1_price}")
elif choose==2:
    print(f"{bike2+2000} will cost you {bike2_price}")
else:
    print("press only 1 or 2")

