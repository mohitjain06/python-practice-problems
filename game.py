import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("comp turn: Snake(s) or Water(w) or Gun(g)? ")
randNo = random.randint(1,3)
if randNo==1:
     comp ='s'
elif randNo==2:
    comp ='w'
elif randNo==3:
    comp ='g'
    

you = input("Your turn: Snake(s) or Water(w) or Gun(g)? ")
a = gamewin(comp,you)


print(f"Comp choose {comp}")
print(f"You choose {you}")

if a==None:
    print("The game is tie")
elif a:
    print("You win the game")
else:
    print("You lose the game")
