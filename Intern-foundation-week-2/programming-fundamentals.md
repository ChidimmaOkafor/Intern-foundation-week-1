# Programming Fundamentals

Introduction

Programming fundamentals are the basic concepts every programmer must understand before building software. These concepts help developers write, read, and maintain code effectively.

---

1. Variables

What is a Variable?

A variable is a container used to store data in a program. The value stored in a variable can change during program execution.

Example

name = "Chidimma"
age = 20

print(name)
print(age)

---

2. Data Types

What are Data Types?

Data types define the kind of value a variable can store.

Common Data Types

Data Type| Description| Example
String| Text data| ""Hello""
Integer| Whole numbers| "10"
Float| Decimal numbers| "3.14"
Boolean| True or False values| "True"
List| Collection of items| "[1, 2, 3]"

Example

name = "John"       # String
age = 25            # Integer
height = 1.75       # Float
is_student = True   # Boolean
scores = [80, 90]   # List

---

3. Operators

What are Operators?

Operators perform operations on values and variables.

Arithmetic Operators

a = 10
b = 5

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division

Comparison Operators

print(10 > 5)
print(10 == 5)
print(10 != 5)

Logical Operators

print(True and False)
print(True or False)
print(not True)

---

4. Conditionals

What are Conditionals?

Conditionals allow programs to make decisions based on conditions.

Example

score = 75

if score >= 70:
    print("Pass")
elif score >= 50:
    print("Average")
else:
    print("Fail")

---

5. Loops

What are Loops?

Loops repeat a block of code multiple times.

For Loop

for number in range(5):
    print(number)

While Loop

count = 1

while count <= 5:
    print(count)
    count += 1

---

6. Functions

What is a Function?

A function is a reusable block of code that performs a specific task.

Example

def greet(name):
    print("Hello", name)

greet("Chidimma")

Function with Return Value

def add(a, b):
    return a + b

result = add(10, 5)
print(result)

---

7. Arrays/Lists

What is a List?

A list stores multiple items in a single variable.

Example

fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
print(fruits[1])

Adding an Item

fruits.append("Mango")
print(fruits)

---

8. Objects/Dictionaries

What is a Dictionary?

A dictionary stores data as key-value pairs.

Example

student = {
    "name": "Chidimma",
    "age": 20,
    "course": "Computer Science"
}

print(student["name"])

Adding a New Value

student["level"] = 300
print(student)lm

---

9. Error Handling

What is Error Handling?

Error handling helps prevent a program from crashing when an error occurs.

Example

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input. Please enter a number.")

---

10. File Handling

What is File Handling?

File handling allows programs to create, read, update, and delete files.

Writing to a File

file = open("sample.txt", "w")
file.write("Hello World")
file.close()

Reading a File

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

---

11. Basic Object-Oriented Programming (OOP)

What is OOP?

Object-Oriented Programming is a programming style that organizes code using classes and objects.

Class and Object Example

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

student1 = Student("Chidimma")
student1.introduce()

---

12. Basic Data Structures

What are Data Structures?

Data structures are ways of organizing and storing data efficiently.

List

numbers = [1, 2, 3, 4]

Dictionary

person = {
    "name": "John",
    "age": 25
}

Tuple

coordinates = (10, 20)

Set

unique_numbers = {1, 2, 3, 4}

---

Conclusion

Programming fundamentals form the foundation of software development. Understanding variables, data types, operators, conditionals, loops, functions, lists, dictionaries, error handling, file handling, object-oriented programming, and basic data structures is essential for becoming a successful programmer.  
