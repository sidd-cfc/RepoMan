# def div42by(divideby):
#     try:
#         return 42 / divideby
#     except ZeroDivisionError:
#         print('Error: You tried to divide things by zero.')

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

print('How many cats do you have?')
numCats=input()
try:
    if int(numCats) >= 4:
        print('You a crazy cat lady')
    else:
        print('That is a good number of cats to keep.')    
except ValueError:
    print('Error:twoYou should be putting a number and not a string.')    