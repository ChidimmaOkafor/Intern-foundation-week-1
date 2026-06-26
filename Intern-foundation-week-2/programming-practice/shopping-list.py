def display_shopping_list(items):
    """Display all items in the shopping list."""
    print("\nShopping List:")
    for item in items:
        print(f"- {item}")


shopping_items = [
    "Headphones",
    "Chocolates",
    "Ice Cream"
]

display_shopping_list(shopping_items)

item_to_remove = "Headphones"

if item_to_remove in shopping_items:
    shopping_items.remove(item_to_remove)
    print(f"\n'{item_to_remove}' has been removed.")
else:
    print(f"\n'{item_to_remove}' is not in the shopping list.")

display_shopping_list(shopping_items)
