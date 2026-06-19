def grade(score):
    score = int(score)

    if score < 0 or score > 100:
        return "Invaild score"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "E"


score = input("Enter a score")
result = grade(score)
print(result)
