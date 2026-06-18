def checker(number):
    number = int(number)
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"


def sign(number):
    number = int(number)
    if number > 0:
        return "The number is positive"
    elif number < 0:
        return "The number is negative"
    else:
        return "The number is zero"


number = input("Enter a number:  ")
result = checker(number), sign(number)
print(result)
