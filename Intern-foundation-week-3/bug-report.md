# Bug Report

## Title

Program Crashes When Dividing by Zero

## Summary

The calculator program crashes when a user enters 0 as the divisor. The application does not handle division by zero and terminates with an error.

## Environment

* Operating System: Windows 11
* Python Version: 3.12
* IDE: Visual Studio Code

## Steps to Reproduce

1. Open the calculator program.
2. Enter a number for the dividend (e.g., 10).
3. Enter 0 as the divisor.
4. Run the division operation.

## Expected Result

The program should display a user-friendly message indicating that division by zero is not allowed.

## Actual Result

The program crashes and stops execution.

## Error Message or Screenshot

```python
ZeroDivisionError: division by zero
```

## Root Cause

The code performed a division operation without checking whether the divisor was zero.

## Fix Applied

Added input validation before performing the division operation. If the divisor is zero, the program displays an error message instead of executing the division.

Example fix:

```python
if divisor == 0:
    print("Division by zero is not allowed.")
else:
    print(dividend / divisor)
```

## How I Tested the Fix

1. Ran the program with divisor set to 0.
2. Verified that the error message was displayed.
3. Ran the program with valid divisors such as 2, 5, and 10.
4. Confirmed that correct results were returned.
5. Confirmed that the program no longer crashes.

## Status

Fixed


