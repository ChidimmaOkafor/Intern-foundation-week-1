file = open("student.txt", "r")
print(file.read())
'''
Error Observed
FileNotFoundError
Root Cause
The file being opened does not exist.

'''

try:
    with open("student.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")
'''
Fix Explanation
Used exception handling to prevent program failure.

'''
