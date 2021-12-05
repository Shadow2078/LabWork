'''
 N students take K apples and distribute them among each other evenly. The remaining

(the indivisible) part remains in the basket. How many apples will each single student

get? How many apples will remain in the basket? The program reads the numbers N and

K. It should print the two answers for the questions above.


'''
Students=int(input("Enter number of Students"))
Apples=int(input("Enter number of Apples in the basket"))
a=Students//Apples
print(a)
b=Students%Apples
print(b)
