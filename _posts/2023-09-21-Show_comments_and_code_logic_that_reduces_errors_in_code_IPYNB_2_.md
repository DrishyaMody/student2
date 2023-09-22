---
comments: True
layout: post
title: Show comments and code logic that reduces errors in code with try / catch statements.
type: hacks
courses: {'csp': {'week': 5}}
---

```python
# Example: A function to divide two numbers

def divide_numbers(dividend, divisor):
    try:
        # Attempt to perform the division
        result = dividend / divisor

        # Return the result if successful
        return result

    except ZeroDivisionError as zde:
        # Handle division by zero error
        print(f"Error: Division by zero is not allowed. {zde}")
        return None

    except TypeError as te:
        # Handle type error (e.g., if either dividend or divisor is not a number)
        print(f"Error: Invalid input. {te}")
        return None

# Test cases
result = divide_numbers(10, 2)  # Should return 5.0
if result is not None:
    print(f"Division result: {result}")

result = divide_numbers(10, 1)  # Should handle division by zero error
if result is not None:
    print(f"Division result: {result}")

result = divide_numbers("10", 5)  # Should handle type error
if result is not None:
    print(f"Division result: {result}")
```

    Division result: 5.0
    Division result: 10.0
    Error: Invalid input. unsupported operand type(s) for /: 'str' and 'int'

