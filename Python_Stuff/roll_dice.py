import random

print("Welcome to the Dice roller")
roll1= random.randint(1,6)
roll2= random.randint(1,6)
Total= roll1+roll2
print(f"You rolled a {roll1} and {roll2}  (Total comes to {Total})!")
