---
comments: True
layout: post
title: Homework Hacks for Boolean team teach
courses: {'csp': {'week': 8}}
type: hacks
---

```python
#Popcorn Hack
num1 = 5
num2 = 7
are_equal = num1 == num2 

print(are_equal)

```

    False



```python
#Popcorn Hack
num1 = 5
num2 = 7
are_not_equal = num1 == num2
print(are_not_equal)
```

    False



```python
#Popcorn Hack
num1 = 2
num2 = 8

is_greater_than= num1 > num2
print(is_greater_than)
```

    False



```python
#Popcorn Hack
grade = 90
result = grade > 70 and grade < 100
print(result)
grade = 50
result = grade > 70 and grade < 100
print(result)




score = 170
highscore = 150
lives = 2
result = (score > highscore) or (lives>1)



```

    True
    False



```python

#Popcorn Hack
num1 = 5
num2 = 10


sum = num1 + num2 

if sum>100: 
    print('100')
else:
    print(sum)
```

    15



```python
#Popcorn Hack
KidGrade= 85

if KidGrade >= 85 : 
    print("no need for tutoring")
else :
    print('Needs tutoring')
```

    no need for tutoring



```python
#Homework Hack1


#True Boolean Expression
student1= 95
student2= 82
student3= 91

average= (student1+student2+student3)/3

is_greater_than = average >= 85
print(is_greater_than)


#False Boolean Expression
student1= 79
student2= 81
student3= 70

average= (student1+student2+student3)/3

is_greater_than = average >= 85
print(is_greater_than)

```

    True
    False



```python
#Homework Hack2
temperature= 19
weather = 'stormy'

can_go_outside= weather == 'stormy' and temperature>=20

print(can_go_outside)


```

    False

