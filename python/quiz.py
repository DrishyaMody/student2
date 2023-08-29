#Asking name before quiz
name=input("What is your name?")
print(f'Hi {name}! Are you ready for the quiz!')
score=0


#Question 1 sequence
question1=input('How many planets are in the solar system')
print(f'{question1}')
if question1 == '8':
    print('Great Job! Ready for the next question?')
    score= score +1
else:
     print ('Sorry that is incorrect')
     


#Question 2 Sequence
question2=input('What sport does Lionel Messi play?')
print(f'{question2}')
if question2== 'soccer':
    print('Great Job! Ready for the last question?')
    score=score+1
elif question2== 'Soccer':
    print('Great Job! Ready for the last question?')
    score=score+1
else: 
     print ('Sorry that is incorrect')


#Question 3 sequence
question3=input('How many continents are there?')
if question3=='7':
    print('Great Job! Ready for your score?')
    score=score+1
else:
    print ('Sorry that is incorrect')


#Score/percentage calculation
percentage = (score/3)*100

print (f'Your score is {percentage}%')






