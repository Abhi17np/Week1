# Grocery Store Inventory Management System

# Initialize an empty inventory dictionary to store item information
inventory = {}

# Function to add a new item to the inventory
def add_item():
    item_name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: $"))
    inventory[item_name] = {"quantity": quantity, "price": price}
    print(f"{item_name} has been added to the inventory.")

# Function to update the quantity of an existing item
def update_quantity():
    item_name = input("Enter the name of the item to update: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name]["quantity"] = new_quantity
        print(f"Quantity of {item_name} has been updated to {new_quantity}.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to view the current inventory
def view_inventory():
    print("Current Inventory:")
    for item, details in inventory.items():
        print(f"{item}: Quantity - {details['quantity']}, Price - ${details['price']}")

# Function to remove an item from the inventory
def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} has been removed from the inventory.")
    else:
        print(f"{item_name} is not in the inventory.")

# Main program loop
while True:
    print("\nGrocery Store Inventory Management System")
    print("1. Add new item")
    print("2. Update item quantity")
    print("3. View inventory")
    print("4. Remove item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

