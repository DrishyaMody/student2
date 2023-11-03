---
comments: True
layout: post
title: Team Teach on Parameters, Algorithims, and Return Values
courses: {'csp': {'week': 9}}
type: hacks
---

## 3.12-3.13 Developing Procedures

## What is a procedure?

A procedure is a named group of programming instructions

2 Main Types of Procedures:
- Procedure that returns a value of data
- Procedure that executes a block of statements

## Learning Objective:
Be able to look at code and determine the purpose, and be able to write a procedure to manage complexity of program. understand the following terms and what they look like as well as how to use them in code

- Procedure Parameters: variables that are defined within the procedure's parentheses and serve as placeholders for values that can be passed to the procedure when it is called, allowing the procedure to operate on different data or values each time it is executed.
- Procedure Algorithms: a step-by-step set of instructions that defines a specific task or operation to be performed within a computer program
- Procedure Return Values: data or results that a procedure can send back to the part of the program that called it, allowing the procedure to provide information or perform a specific task and then share the outcome with the rest of the program.

## Name, Parameters, Algorithm, Return Values, and Calling a Procedure




```python
## Example of Procedure that Updates A Quiz Grade
def updatequiz(currentgrade, quizgrade):
    if quizgrade > currentgrade:
        currentgrade = quizgrade
    return currentgrade

currentgrade = 75
quizgrade = 88
currentgrade = updatequiz(currentgrade, quizgrade)
print(currentgrade)
```

    88


## Popcorn Hack #1:
Identify the name of the procedure below, tell us the purpose and parameters of the procedure and identify the algorithm return value:

- Name: updateweather
- Parameters: currentweather, weather
- Return Value:  Currentgrade
- Calling Procedure Line: Line 11


```python
def updateweather(currentweather, weather):     
    if currentweather> weather:                 
        weather = currentweather               
        print("today is warmer than yesterday") 
    else:
        print("today is colder than yesterday")
    return currentgrade   

currentweather = 71
weather = 66
currentgrade = updateweather(currentweather, weather)    #this line calls the procedure
print("the temperature right now is", currentweather, "degrees")
```

    today is warmer than yesterday
    the temperature right now is 71 degrees


## Costructing Classes for Names & Data with Procedures


```python
# Class Construction
class Short:
    name = ""
    height = 0

class Tall:
    name = ""
    height = 0

# Procedure to Classify as Short or Tall
def classify_person(name, height):
    if height < 70:
        short_person = Short()
        short_person.name = name
        return short_person
    else:
        tall_person = Tall()
        tall_person.name = name
        return tall_person
```

Class Definitions: The code defines two classes, "Short" and "Tall," each having two attributes: name and height. These attributes can be used to store the name and height of individuals.

Classification Procedure: The classify_person function takes two parameters: name and height. Depending on the provided height, it creates an instance of either the "Short" or "Tall" class. It sets the name attribute for the person and returns the corresponding instance.

## Popcorn Hack #2:
Use the example above to use a procedure to create two classes of your choosing. Create at least 2 objects and class them with your procedure


```python
# Popcorn Hack 2
class tall: 
    name= 'Damian Lillard'
    height = '74'

class short:
    name = "Kaiyu Sugiyama"
    height = '65'

def classify_person(name, height):
    if height < 70:
        short_person = Short()
        short_person.name = name
        return short_person
    else:
        tall_person = Tall()
        tall_person.name = name
        return tall_person
```

## Calling Methods of an Object w/ Procedures


```python
# Creating Classes
class Short:
    name = ""
    height = 0

class Tall:
    name = ""
    height = 0

#Procedure to classify as short or tall
def classify_height(name, height):
    if height < 70:
        short_person = Short()
        short_person.name = name
        return short_person
    else:
        tall_person = Tall()
        tall_person.name = name
        return tall_person

# Create objects and classify them as short or tall
person1 = classify_height("Nihar", 12)
person2 = classify_height("Will", 76)
person3 = classify_height("Jayden", 75)
person4 = classify_height("Howie", 70)

# Display results for all four objects
for person in [person1, person2, person3, person4]:
    print(f"{person.name} is {'Short' if person is Short else 'Tall'}.")


```

    Nihar is Tall.
    Will is Tall.
    Jayden is Tall.
    Howie is Tall.


## HW Hacks!!
1. Create a procedure that replaces a value with a new one (ex. update height)
2. Create a procedure that constructs classes of your choosing and create at least 4 objects to be sorted into your classes. Call your procedure to display your objects.


```python
# HW Hack 1
# Procedure to replace a value with a new one
def replace_value(data, old_value, new_value):
    if old_value in data:
        index = data.index(old_value)
        data[index] = new_value
        print(f"Value {old_value} replaced with {new_value}. New data: {data}")
    else:
        print(f"Value {old_value} not found in the data.")

# Example usage
data_list = [1, 2, 3, 4, 5]
replace_value(data_list, 3, 10)

```

    Value 3 replaced with 10. New data: [1, 2, 10, 4, 5]



```python
# HW Hack 2

# Procedure to create classes and objects
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Creating objects
obj1 = MyClass("Object1", 10)
obj2 = MyClass("Object2", 15)
obj3 = MyClass("Object3", 5)
obj4 = MyClass("Object4", 20)

# Displaying the objects
objects = [obj1, obj2, obj3, obj4]
for obj in objects:
    print(f"Object Name: {obj.name}, Value: {obj.value}")

```

    Object Name: Object1, Value: 10
    Object Name: Object2, Value: 15
    Object Name: Object3, Value: 5
    Object Name: Object4, Value: 20

