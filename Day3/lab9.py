'''
Take username and password from user and check it again for the three times whether the user has entered the right username and password.
if yes then print a message "Logged in Succesfully", if not then print invalid credentials for consequtive 3 times and if the limit exceeds
then  print "Attempt Finished".
'''

for i in range(3):
    username=str(input("Enter your username:"))
    password=str(input("Enter your password:"))
    if username=="Suman" and password=="Suman222":
        print("logged in Successfully")
        break
    
else:
    print("Attempt finished")
