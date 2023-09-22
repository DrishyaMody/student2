---
comments: True
layout: post
title: Show comments and code logic that reduces errors in code with if / else statements.
type: hacks
courses: {'csp': {'week': 5}}
---

```python
# Example: A function to calculate the square root of a number
import math

def calculate_square_root(number):
    # Check if the input is negative
    if number < 0:
        raise ValueError("Input should be a non-negative number.")

    # Use the math.sqrt function to calculate the square root
    result = math.sqrt(number)

    return result

# Test cases
try:
    result = calculate_square_root(9)  # Should return 3.0
    print(f"Square root result: {result}")
except ValueError as ve:
    print(f"Error: {ve}")

try:
    result = calculate_square_root(-1)  # Should raise a ValueError
    print(f"Square root result: {result}")
except ValueError as ve:
    print(f"Error: {ve}")
```

    Square root result: 3.0
    Error: Input should be a non-negative number.

