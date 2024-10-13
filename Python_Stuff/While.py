# spam=1
# while spam<5:
#     print('Hello world')
#     spam=spam+1  

# name=''
# while name !='Siddhesh':
#     print('Please type your name')
#     name=input()
# print('Thank you')

# spam = 0                    # Step 1: Initial value of 'spam' is set to 0
# while spam < 5:              # Step 2: The loop will keep running as long as 'spam' is less than 5
#     spam = spam + 1          # Step 3: Add 1 to 'spam' each time the loop runs
#     if spam == 3:            # Step 4: Check if 'spam' is equal to 3
#         continue             # Step 5: If 'spam' is 3, skip the rest of the code and go to the next loop iteration
#     print('spam is ' + str(spam))  # Step 6: Print 'spam is' followed by the current value of 'spam', except when spam is 3
    
    
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "correctpassword":
        print("Access granted")
        break  # Stop the loop if the correct password is entered
    attempts=attempts + 1
else:
    print("Too many attempts, access denied")
