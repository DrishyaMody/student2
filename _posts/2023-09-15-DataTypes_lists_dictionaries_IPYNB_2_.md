---
toc: True
comments: True
layout: post
title: Datatypes, Lists, Dictionaries
courses: {'csp': {'week': 4}}
type: hacks
---

```python
# Sample of Python Variables

# variable of type string
print("What is the variable name/key?", "value?", "type?", "primitive or collection, why?")
name = "John Doe"
print("name", name, type(name))

```

    What is the variable name/key? value? type? primitive or collection, why?
    name John Doe <class 'str'>



```python
# variable of type integer
print("What is the variable name/key?", "value?", "type?", "primitive or collection, why?")
age = 18
print("age", age, type(age))
```

    What is the variable name/key? value? type? primitive or collection, why?
    age 18 <class 'int'>



```python
# variable of type float
print("What is the variable name/key?", "value?", "type?", "primitive or collection, why?")
score = 90.0
print("score", score, type(score))
```

    What is the variable name/key? value? type? primitive or collection, why?
    score 90.0 <class 'float'>



```python
# variable of type list (many values in one variable)
print("What is variable name/key?", "value?", "type?", "primitive or collection?")
print("What is different about the list output?")
langs = ["Python", "JavaScript", "Java"]
print("langs", langs, type(langs), "length", len(langs))
print("- langs[0]", langs[0], type(langs[0]))
print("- langs[1]", langs[1], type(langs[1]))
print("- langs[2]", langs[2], type(langs[2]))
```

    What is variable name/key? value? type? primitive or collection?
    What is different about the list output?
    langs ['Python', 'JavaScript', 'Java'] <class 'list'> length 3
    - langs[0] Python <class 'str'>
    - langs[1] JavaScript <class 'str'>
    - langs[2] Java <class 'str'>



```python
# variable of type dictionary (a group of keys and values)
print("What is the variable name/key?", "value?", "type?", "primitive or collection, why?")
print("What is different about the dictionary output?")
person = {
    "name": name,
    "age": age,
    "score": score,
    "langs": langs
}
print("person", person, type(person), "length", len(person))
print('- person["name"]', person["name"], type(person["name"]))
print('- person["age"]', person["age"], type(person["age"]))
print('- person["score"]', person["score"], type(person["score"]))
print('- person["langs"]', person["langs"], type(person["langs"]))
```

    What is the variable name/key? value? type? primitive or collection, why?
    What is different about the dictionary output?
    person {'name': 'John Doe', 'age': 18, 'score': 90.0, 'langs': ['Python', 'JavaScript', 'Java']} <class 'dict'> length 4
    - person["name"] John Doe <class 'str'>
    - person["age"] 18 <class 'int'>
    - person["score"] 90.0 <class 'float'>
    - person["langs"] ['Python', 'JavaScript', 'Java'] <class 'list'>



```python
# Define an empty List called InfoDb
InfoDb = []

# InfoDB is a data structure with expected Keys and Values

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "FirstName": "John",
    "LastName": "Mortensen",
    "DOB": "October 21",
    "Residence": "San Diego",
    "Email": "jmortensen@powayusd.com",
    "Owns_Cars": ["2015-Fusion", "2011-Ranger", "2003-Excursion", "1997-F350", "1969-Cadillac"]
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Sunny",
    "LastName": "Naidu",
    "DOB": "August 2",
    "Residence": "Temecula",
    "Email": "snaidu@powayusd.com",
    "Owns_Cars": ["4Runner"]
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Shane",
    "LastName": "Lopez",
    "DOB": "February 27",
    "Residence": "San Diego",
    "Email": "???@powayusd.com",
    "Owns_Cars": ["2021-Insight"]
})

# Print the data structure
print(InfoDb)

```
