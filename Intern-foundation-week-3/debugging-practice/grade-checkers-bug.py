score = 85

if score >= 70:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Fail")

'''
Error Observed
A score of 85 returns A even though the grading logic is incorrect.
'''
"""
Root Cause
Conditions are ordered incorrectly.
"""
score = 85

if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 0 <= score < 70:
    print("Fail")
else:
    print("Invalid score")
'''
Fix Explanation
Used proper score ranges and validation.
'''
