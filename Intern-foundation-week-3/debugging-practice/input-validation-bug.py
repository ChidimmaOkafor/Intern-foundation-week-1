age = int(input("Enter your age: "))
print(age)
'''
Error Observed
ValueError

when the user enters:
abc

Root Cause
int() can only convert valid numeric strings.

'''
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a valid number")

'''
Fix Explanation
Added error handling for invalid user input.

'''
