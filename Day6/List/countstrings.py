#. Write a Python program to count the number
#  of strings where the string length is 2 
#or more and the first and last character are sam
#e from a given list of strings. 
#Sample List : ['abc', 'xyz', 'aba', '1221'] Expected 
#Result : 2 
list=['abc','xyz','aba','1221']
count=0
for i in list:
    if len(list)>2:
        if i[0]==i[len(i)-1]:
            count=count+1
print(count)