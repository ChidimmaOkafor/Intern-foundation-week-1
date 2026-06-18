def calculator(number_1, number_2, operation):
    number_1 = int(number_1)
    number_2 = int(number_2)
    if operation == "+":
        return number_1+number_2
    elif operation == "-":
        return number_1-number_2
    elif operation == "*":
        return number_1-number_2
    elif operation == "/":
        if number_2 == 0:
            return "Enter a valid number"
        else:
            return number_1/number_2
    else:
        return "Invaild operation"


number_1 = input("Enter number 1 :")

operation = input("Enter an Operation  (+,-,/,*): ")

number_2 = input("Enter number 2: ")
result = calculator(number_1, number_2, operation)
print("Result :", result)
