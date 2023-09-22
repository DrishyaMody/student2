---
toc: True
comments: True
layout: post
title: Comments on mathematical program
courses: {'csp': {'week': 5}}
type: hacks
---

```python
import statistics

# Sample list of numbers
data = [12, 18, 24, 32, 42, 55, 67]

# Calculate the mean (average) of the numbers
mean = statistics.mean(data)

# Calculate the standard deviation of the numbers
std_deviation = statistics.stdev(data)

# Display the results
print("List of Numbers:", data)
print("Mean (Average):", mean)
print("Standard Deviation:", std_deviation)

```

    List of Numbers: [12, 18, 24, 32, 42, 55, 67]
    Mean (Average): 35.714285714285715
    Standard Deviation: 20.072487686003495

