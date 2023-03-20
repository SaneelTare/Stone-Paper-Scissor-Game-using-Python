import random
# random is a module which has randint function which is used to get random values from the set

#function is used so we need not use the same code multiple times
def you_win(comp,you):
    if comp==you:
        return None
# if 2 values equal its a tie
# stone o paper p scissor x
# Check for all possibilities when computer chose s
    elif comp=='o':
        if you=='x':
            return False
        elif you=='p':
            return True
        
# Check for all possibilities when computer chose w
    elif comp=='p':
        if you=='o':
            return False
        elif you=='x':
            return True
        
# Check for all possibilities when computer chose g
    elif comp=='x':
        if you=='p':
            return False
        elif you=='o':
            return True

# ---computer chooses randomly using randint
print("Computer turn: Stone(o) paper(p) or scissor(x)?")
rand_No=random.randint(1,3)
if rand_No==1:
    comp='o'
elif rand_No==2:
    comp='p'
elif rand_No==3:
    comp='x'

#user chance to input
you=input("Your turn: stone(o) paper(p) or scissor(x)? ")
# if you!="o" or you!="p" or you!="x":
#     print("enter o p or x as input")
# else:
a=you_win(comp,you)
print(" stone - o paper - p and scissor - x ")
print(f"computer choose {comp}")
print(f"you choose {you}")
if a==None:
    print("game is a tie!")
elif a:
    print("you win!")
else:
    print("you lost!")
