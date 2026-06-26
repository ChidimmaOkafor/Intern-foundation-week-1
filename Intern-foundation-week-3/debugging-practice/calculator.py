def divide(a, b):
    return a/b


print(divide(10, 0))
"""
Error Observed
ZeroDivisionError: division by zero

"""


def divide(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    return a/b


print(divide(10, 0))
"""
Added validation to check if the divisor is zero before performing division
"""
