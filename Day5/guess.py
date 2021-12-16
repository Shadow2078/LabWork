
num=5
while True:
    guess=int(input("Guess the number between 1-9:"))
    if guess>0 and guess==5 and guess<10:
        print("Well,Guessed!")
        break
    
    else:
        print("Enter again")
        continue
