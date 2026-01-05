import random
n=random.randint(1,101)
a=-1
guess=1
while(a!=n):
    guess+=1
    a=int(input("Enter your Guess: "))
    if(a>n):
        print("It is greater,Please enter less number")
    elif(a<n):
        print("Your near to that number,Enter greater number")
print(f"Your guess is correct at {guess} and number is {n}")