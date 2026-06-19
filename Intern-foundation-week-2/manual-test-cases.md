# Test Case ID: TC-001

Feature: Shopping List
Scenario: Add a valid item
Steps:

   Run the shopping list program
   Select “Add item” option
   Enter Rice
   View the shopping list

Expected Result:
   “Rice” should appear in the shopping list

Actual Result:
   Your items:
     1. Rice

Status:
   Pass 

# Test Case ID: TC-002

Feature: Shopping List
Scenario: Add an empty item
Steps:

    Run the program
    Select “Add item”
    Press Enter without typing anything
    View the shopping list

Expected Result:
System should reject empty input and not add it to the list

Actual Result:
    Select option: 1
    Enter item:
    Invalid input: item cannot be empty

Status: 
    Pass

#  Test Case ID: TC-003

Feature: Shopping List
Scenario: Remove an existing item
Steps:

    Run the program
    Add item Rice
    Select “Remove item”
    Enter Rice
    View the list

Expected Result:
    “Rice” should be removed from the shopping list

Actual Result:
    Shopping list is empty.

Status:
     Pass

# Test Case ID: TC-004

Feature: Shopping List
Scenario: Remove an item that does not exist
Steps:

    Run the program
    Add item Beans
    Select “Remove item”
    Enter Sugar

Expected Result:
    System should display a message like “Item not found” and no changes made

Actual Result:
    Enter item to remove: Sugar
    Item not found.

Status:
    Pass

# Test Case ID: TC-005

Feature: Shopping List
Scenario: View an empty shopping list
Steps:

    Run the program
    Ensure no items are added
    Select “View list”

Expected Result:
    System should display “Shopping list is empty”

Actual Result:
    Shopping list is empty.
Status:
    Pass

# Test Case ID: TC-006

Feature: Shopping List
Scenario: View a shopping list with items
Steps:

   Run the program
   Add Rice and Beans
   Select “View list”

Expected Result:
   Both items should be displayed correctly

Actual Result:
   Your items:
   1. Rice and Beans

Status:
   Pass

# Test Case ID: TC-007

Feature: Shopping List
Scenario: Enter invalid input
Steps:

    Run the program
    Enter a non-menu option like 999 or abc

Expected Result:
    System should show error message and request valid input

Actual Result:
    Select option: abc
    Invalid option.
Status:
     Pass
    
# Test Case ID: TC-008

Feature: Shopping List
Scenario: Exit the program
Steps:

   Run the program
   Select “Exit” option

Expected Result:
    Program should terminate safely without errors

Actual Result:
    Select option: 4
    Goodbye.

Status:
    Pass