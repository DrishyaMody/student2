---
comments: True
layout: post
title: Tester Function
type: hacks
courses: {'csp': {'week': 5}}
---

```python

# Example of a tester function for validating program functionality without try/catch
def tester_function(program_input):
    if program_input < 0:
        print("Error: Input should be a positive number.")
        return  # Exit the function if input is invalid

    # Use if/else statements to handle different cases
    result = some_function(program_input)

    # Check if the result is as expected
    if result == expected_result:
        print("Test Passed")
    else:
        print("Test Failed")

# Example of a function with if/else statements
def some_function(input_value):
    if input_value < 0:
        return "Input is negative"
    elif input_value < 10:
        return "Less than 10"
    else:
        return "Greater than or equal to 10"

# Testing the function
expected_result = "Less than 10"
tester_function(5)  # Should print "Test Passed"
tester_function(-5)  # Should print "Error: Input should be a positive number."
tester_function(15)  # Should print "Test Failed"

```

    Test Passed
    Error: Input should be a positive number.
    Test Failed

