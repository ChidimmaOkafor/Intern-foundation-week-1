fruits = ["apple", "banana", "orange"]

fruits.remove("mango")

print(fruits)

"""
ValueError: list.remove(x): x not in list
"""

fruits = ["apple", "banana", "orange"]
if "mango" in fruits:
    fruits.remove("mango")
else:
    print("Item not found")
print(fruits)
""" 
Check whether the item exists before attempting removal 
"""
