#Asking name before quiz
name=input("What is your name?")
print(f'Hi {name}! Are you ready for the quiz!')
score=0


#Question 1 sequence
question1=input('What python version should we be using?')
print(f'{question1}')
if question1 == '3.11.4':
    print('Great Job! Ready for the next question?')
    score= score +1
else:
     print ('Sorry that is incorrect')
     


#Question 2 Sequqnce
question2=input('If you see many lines of code in order, what would College Board call it?')
print(f'{question2}')


