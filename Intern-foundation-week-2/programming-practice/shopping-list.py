shopping_list = []
print("Shopping list")
shopping_list.append("Headphones")
shopping_list.append("chocolates")
shopping_list.append("icecream")
for item in shopping_list:
    print(item)
shopping_list.remove("Headphones")
print("Update Shopping List")
for item in shopping_list:
    print(item)
