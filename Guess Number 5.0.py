#This gives you chance to try even after you lost and restart game
#guess in range with full chance given back if not in range
#Game start option
#Gives you count of chances after each guess

import random
import math

def main():
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))

    x=random.randint(lower,upper)
    n=0
    y=int(input("Number of tries you want:-"))
    guess=int()
    z='T'
    p='F'
    while z!=p:
        while x!=guess:
            guess=int(input("Enter your guess:"))
            if guess in range(lower,upper):pass
            elif guess not in range(lower,upper):
                print("Guess in range")
                print("You've",y-n,"chances left ")
                continue
                
            if x==guess:
                print('You are right')
                break
            elif x>guess:
                n=n+1
                if n==y:
                     z=str(input('Wanna guess again?T/F:'))
                     if z=='F': break
                elif n!=y:
                    print('Guess Higher')
                    print("You've",y-n,"chances left ")
            elif x<guess:
                n=n+1
                if n==y:
                    z=str(input('Wanna guess again?T/F:'))
                    if z=='F': break
                elif n!=y:
                    print('Guess Lower')
                    print("You've",y-n,"chances left ")
        z=str(input('Wanna play again?T/F:'))
        if z=='T':
            main()
        elif z=='F':
            break
ask=str(input('Do you wanna start the game{Y/N}:-'))
if ask=='Y':main()
