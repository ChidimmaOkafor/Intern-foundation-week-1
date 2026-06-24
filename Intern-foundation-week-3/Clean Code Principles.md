# Clean Code Principles

## Introduction

Clean code is code that is easy to read, understand, maintain, and improve. Writing code that works is important, but writing code that other developers can easily understand is equally important. Clean code helps teams collaborate effectively and reduces bugs.

---

# 1. Meaningful Naming

Variable names, function names, and file names should clearly describe their purpose.

## Bad Example

```python
x = 5000
y = 0.1
z = x * y
```

## Clean Example

```python
salary = 5000
tax_rate = 0.1
tax_amount = salary * tax_rate
```

### Why It Is Better

The names clearly explain what each variable represents.

---

# 2. Small Functions

Functions should do one specific task.

## Bad Example

```python
def process_user():
    validate_user()
    save_user()
    send_email()
    generate_report()
```

## Clean Example

```python
def validate_user():
    pass

def save_user():
    pass

def send_welcome_email():
    pass
```

### Why It Is Better

Each function has one responsibility, making the code easier to test and maintain.

---

# 3. Clear Folder Structure

Projects should be organized logically.

## Bad Structure

```text
project/
├── file1.py
├── file2.py
├── file3.py
├── file4.py
```

## Better Structure

```text
project/
├── src/
│   ├── users.py
│   └── products.py
├── tests/
│   └── test_users.py
├── docs/
└── README.md
```

### Why It Is Better

Files are easier to locate and maintain.

---

# 4. Avoiding Duplicate Code

Do not repeat the same code in multiple places.

## Bad Example

```python
print("Welcome John")
print("Welcome Mary")
print("Welcome David")
```

## Clean Example

```python
def welcome_user(name):
    print(f"Welcome {name}")

welcome_user("John")
welcome_user("Mary")
welcome_user("David")
```

### Why It Is Better

Changes only need to be made in one place.

---

# 5. Comment Only When Necessary

Code should be clear enough to explain itself.

## Bad Example

```python
# Add two numbers
result = number1 + number2
```

## Better Example

```python
total_price = item_price + shipping_fee
```

### When Comments Are Useful

* Explaining complex logic
* Explaining business rules
* Providing important warnings

Example:

```python
# Passwords must be hashed before storage for security
```

---

# 6. Proper Formatting

Consistent formatting improves readability.

## Bad Example

```python
if(age>=18):print("Adult")
```

## Clean Example

```python
if age >= 18:
    print("Adult")
```

### Why It Is Better

The code is easier to read and review.

---

# 7. Keep Code Readable

Write code that is easy for other developers to understand.

## Bad Example

```python
if a:
    if b:
        if c:
            print("Approved")
```

## Better Example

```python
if is_valid_user and has_permission and account_is_active:
    print("Approved")
```

### Why It Is Better

The intention of the code is clear.

---

# 8. Avoid Hardcoded Values

Hardcoded values are values written directly inside the code.

## Bad Example

```python
discount = price * 0.15
```

## Better Example

```python
DISCOUNT_RATE = 0.15
discount = price * DISCOUNT_RATE
```

### Why It Is Better

The value can be updated easily without searching through the entire project.

---

# 9. Environment Variables

Environment variables store configuration values outside the code.

Examples:

* Database passwords
* API keys
* Secret tokens
* Application settings

## Bad Example

```python
API_KEY = "123456789"
```

## Better Example

```python
import os

API_KEY = os.getenv("API_KEY")
```

### Why It Is Better

Sensitive information is not exposed in the source code.

---

# Why Code Readability Is Important

Code is read more often than it is written. Readable code:

* Makes debugging easier
* Helps team collaboration
* Reduces mistakes
* Speeds up code reviews
* Makes future updates easier

---

# Conclusion

Clean code is not just about making programs work. It is about writing code that other developers can easily read, understand, maintain, and improve. By using meaningful names, small functions, clear folder structures, avoiding duplication, minimizing unnecessary comments, formatting code properly, avoiding hardcoded values, and using environment variables, developers can create higher-quality software.
