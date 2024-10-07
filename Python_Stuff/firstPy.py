# print(' This is a test file')
# print(' Chelsea!!!' * 5)
# print('Premier league Champions '*6,'European Champions '*2)
# print(' KTBFFH')

### Career Tenure 
print('Hello There!')
print('Whats your name ?')
MyName=input()
print('It is nice to meet you '+MyName)
print('Which year did you start your career?') #ask which year did the person start their career
CareerStartYear=int(input())
from datetime import datetime
current_year=datetime.now().year
careerduration=current_year-CareerStartYear
print('It been '+ str(careerduration)+ ' years since you started your career') # Display the tenure by subtracting the CareerStartYear and current_year  