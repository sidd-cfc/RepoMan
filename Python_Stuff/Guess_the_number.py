#Guess the number game
import random

print('Heyoo!! What is your name? ')
name=input()

print('Well, ' +name+ ', I am thinking of a number between 0 and 10.')
secretNumber=random.randint(3,5)

for guessesTaken in range(0,4):
    print('Take a guess')
    guess=int(input())

    if guess<secretNumber:
        print('Its too low')
    elif guess>secretNumber:
        print('Its too high')
    else:
        break    

if guess==secretNumber:
    print('Good Job!! '+ name + ' You guessed my number in '+ str(guessesTaken)+ ' guesses')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))

