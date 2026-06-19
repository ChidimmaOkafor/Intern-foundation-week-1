 
shopping_list = []

while True:
    print("\n=== SHOPPING LIST ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

    choice = input("Select option: ").strip()

    if choice == "1":
        item = input("Enter item: ").strip()

        if item == "":
            print("Invalid input: item cannot be empty.")
        else:
            shopping_list.append(item)
            print(f"{item} added.")

    elif choice == "2":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nYour items:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")