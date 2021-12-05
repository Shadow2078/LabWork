# a School decided to replace the desks in three classrooms. Each desk sits two students.
#Given the number of students in each class printthe smallest possible number of desks.
#that can be purchased.
#the program should read three intehers: the numner of students in each of the three 
#classes, a , b and c respectively.
#Suppose in the first test there are three groups. The first group has 20 students and thus need 
#desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

G1=int(input("Enter the number of student in first class:"))
G2=int(input("Enter the number of students in second class:"))
G3=int(input("Enter the number of students in third class:"))

D1=(G1//2)
print(f"The required number of desk for first class is {D1}")

D2=(G2//2)
print(f"the required numner of desks for second class is {D2}")

D3=(G3//3)
print(f"the required number of desks for second class is {D3}")
