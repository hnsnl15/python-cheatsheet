## Table of Contents

1. [Python Cheatsheet](#python-cheatsheet)
   1.1. [Variables and Data Types](#variables-and-data-types)
   1.2. [Basic Operations](#basic-operations)
   1.3. [Conditional Statements](#conditional-statements)
   1.4. [Loops](#loops)
   1.5. [Functions](#functions)
   1.6. [Lists](#lists)
   1.7. [Strings](#strings)
   1.8. [Dictionaries](#dictionaries)
   1.9. [Error Handling](#error-handling)
   1.10. [File Handling](#file-handling)
   1.11. [Modules and Libraries](#modules-and-libraries)

2. [Python Data Structures Cheatsheet](#python-data-structures-cheatsheet)
   2.1. [Lists](#lists)
   2.2. [Tuples](#tuples)
   2.3. [Sets](#sets)
   2.4. [Dictionaries](#dictionaries)
   2.5. [Strings](#strings)
   2.6. [Queues (using `collections.deque`)](#queues-using-collectionsdeque)
   2.7. [Stacks (using lists)](#stacks-using-lists)
   2.8. [Comprehensions](#comprehensions)
   2.9. [Iterating](#iterating)
   2.10. [Special Data Structures](#special-data-structures)

3. [Python Operators Cheatsheet](#python-operators-cheat-sheet)
   3.1. [Arithmetic Operators](#arithmetic-operators)
   3.2. [Comparison Operators](#comparison-operators)
   3.3. [Logical Operators](#logical-operators)
   3.4. [Assignment Operators](#assignment-operators)
   3.5. [Identity Operators](#identity-operators)
   3.6. [Membership Operators](#membership-operators)
   3.7. [Bitwise Operators](#bitwise-operators)
   3.8. [Ternary Operator](#ternary-operator)

## Python Cheatsheet

### Variables and Data Types

```python
# Variables
variable_name = value

# Data Types
integer = 42
float_number = 3.14
string = "Hello, World!"
boolean = True
list = [1, 2, 3]
tuple = (1, 2, 3)
dictionary = {"key": "value"}
```

### Basic Operations

```python
# Arithmetic Operations
result = 5 + 3
result = 7 - 2
result = 4 * 6
result = 10 / 2
result = 11 % 3

# String Concatenation
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2

# List Operations
my_list = [1, 2, 3]
my_list.append(4)
my_list.pop()
```

### Conditional Statements

```python
if condition:
    # Code to run if the condition is True
elif another_condition:
    # Code to run if the first condition is False and this one is True
else:
    # Code to run if all conditions are False
```

### Loops

```python
# For Loop
for item in iterable:
    # Code to execute for each item

# While Loop
while condition:
    # Code to execute as long as the condition is True
```

### Functions

```python
def function_name(parameters):
    # Function code
    return result

# Calling a Function
result = function_name(argument_value)
```

### Lists

```python
# Create a List
my_list = [1, 2, 3]

# Accessing Elements
element = my_list[0]

# Slicing
sublist = my_list[1:3]

# List Comprehension
squared_numbers = [x**2 for x in my_list]

# List Methods
my_list.append(4)
my_list.extend([5, 6])
my_list.remove(3)
```

### Strings

```python
# String Methods
my_string = "Hello, World!"
length = len(my_string)
uppercase = my_string.upper()
lowercase = my_string.lower()
substring = my_string[7:12]
```

### Dictionaries

```python
# Create a Dictionary
my_dict = {"key1": "value1", "key2": "value2"}

# Accessing Values
value = my_dict["key1"]

# Adding and Modifying
my_dict["key3"] = "value3"
my_dict["key1"] = "new_value"

# Dictionary Methods
keys = my_dict.keys()
values = my_dict.values()
```

### Error Handling

```python
try:
    # Code that may raise an exception
except ExceptionType as e:
    # Handle the exception
finally:
    # Code that always runs
```

### File Handling

```python
# Opening a File
file = open("filename.txt", "r")  # "r" for reading, "w" for writing

# Reading from a File
content = file.read()
line = file.readline()

# Writing to a File
file.write("Hello, File!")

# Closing a File
file.close()
```

### Modules and Libraries

```python
# Importing a Module
import module_name

# Using a Module
result = module_name.function_name()
```

This cheatsheet covers some of the fundamental aspects of Python programming. Keep in mind that Python is a versatile language, and there are many more concepts and libraries to explore.

## Python Data Structures Cheatsheet

### Lists

```python
# Creating a List
my_list = [1, 2, 3, 4]

# Accessing Elements
first_element = my_list[0]
last_element = my_list[-1]

# Slicing
subset = my_list[1:3]

# Modifying Elements
my_list[0] = 5

# List Methods
my_list.append(6)
my_list.extend([7, 8])
my_list.remove(3)
my_list.pop()
my_list.insert(2, 9)
my_list.sort()
my_list.reverse()
```

### Tuples

```python
# Creating a Tuple
my_tuple = (1, 2, 3)

# Accessing Elements
element = my_tuple[0]

# Tuple Unpacking
x, y, z = my_tuple

# Immutable - Cannot be modified
```

### Sets

```python
# Creating a Set
my_set = {1, 2, 3}

# Adding and Removing Elements
my_set.add(4)
my_set.remove(2)

# Set Operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
```

### Dictionaries

```python
# Creating a Dictionary
my_dict = {"key1": "value1", "key2": "value2"}

# Accessing Values
value = my_dict["key1"]

# Adding and Modifying Values
my_dict["key3"] = "value3"
my_dict["key1"] = "new_value"

# Dictionary Methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
del my_dict["key2"]
```

### Strings

```python
# Creating a String
my_string = "Hello, World!"

# String Operations
length = len(my_string)
uppercase = my_string.upper()
lowercase = my_string.lower()
substring = my_string[7:12]

# String Methods
split_list = my_string.split(",")
concatenation = " ".join(split_list)
```

### Queues (using `collections.deque`)

```python
from collections import deque

# Creating a Queue
queue = deque()

# Enqueue and Dequeue
queue.append(1)  # Enqueue
item = queue.popleft()  # Dequeue
```

### Stacks (using lists)

```python
# Creating a Stack
stack = []

# Push and Pop
stack.append(1)  # Push
item = stack.pop()  # Pop
```

### Comprehensions

```python
# List Comprehension
squared_numbers = [x**2 for x in my_list]

# Dictionary Comprehension
squared_dict = {x: x**2 for x in my_list}
```

### Iterating

```python
# Looping through a Sequence
for item in my_list:
    print(item)

# Iterating through a Dictionary
for key, value in my_dict.items():
    print(key, value)
```

### Special Data Structures

#### NamedTuples

```python
from collections import namedtuple

# Creating a NamedTuple
Person = namedtuple("Person", ["name", "age"])
person = Person("Alice", 30)
print(person.name, person.age)
```

#### DefaultDicts

```python
from collections import defaultdict

# Creating a DefaultDict
my_dict = defaultdict(int)
my_dict["key"] += 1  # Avoids KeyErrors
```

This cheatsheet should help you understand and work with Python's various data structures effectively. Remember that these are just the basics, and each data structure offers more advanced capabilities.

## Python Operators Cheatsheet

### Arithmetic Operators

```python
# Addition
result = x + y

# Subtraction
result = x - y

# Multiplication
result = x * y

# Division
result = x / y

# Floor Division (integer division)
result = x // y

# Modulus (remainder)
result = x % y

# Exponentiation
result = x ** y
```

### Comparison Operators

```python
# Equal to
x == y

# Not equal to
x != y

# Greater than
x > y

# Less than
x < y

# Greater than or equal to
x >= y

# Less than or equal to
x <= y
```

### Logical Operators

```python
# Logical AND
result = condition1 and condition2

# Logical OR
result = condition1 or condition2

# Logical NOT
result = not condition
```

### Assignment Operators

```python
# Assignment
x = y

# Add and assign
x += y  # Equivalent to x = x + y

# Subtract and assign
x -= y  # Equivalent to x = x - y

# Multiply and assign
x *= y  # Equivalent to x = x * y

# Divide and assign
x /= y  # Equivalent to x = x / y

# Modulus and assign
x %= y  # Equivalent to x = x % y

# Floor Division and assign
x //= y  # Equivalent to x = x // y

# Exponentiation and assign
x **= y  # Equivalent to x = x ** y
```

### Identity Operators

```python
# is - True if both variables are the same object
x is y

# is not - True if both variables are not the same object
x is not y
```

### Membership Operators

```python
# in - True if a sequence contains an item
item in sequence

# not in - True if a sequence does not contain an item
item not in sequence
```

### Bitwise Operators

```python
# Bitwise AND
result = x & y

# Bitwise OR
result = x | y

# Bitwise XOR
result = x ^ y

# Bitwise NOT
result = ~x

# Bitwise Left Shift
result = x << y

# Bitwise Right Shift
result = x >> y
```

### Ternary Operator

```python
# Conditional expression (Ternary Operator)
value_if_true if condition else value_if_false
```

This cheat sheet covers the most commonly used Python operators. Understanding these operators is essential for working with Python and performing various operations in your code.
