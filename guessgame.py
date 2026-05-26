import random


randNo = random.randint(1,100)
userguess = None
guesses = 0
while(userguess!=randNo):
    userguess = int(input("Guess the number? "))
    guesses +=1
    if randNo==userguess:
        print("You guess it right")
    else:
        if(randNo>userguess):
            print("You guess it wrong! Enter larger number")
        elif(randNo<userguess):
            print("You guess it wrong! Enter smaller number")

print(f"You guess the right number in {guesses} guesses")