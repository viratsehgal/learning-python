inventory = ["apple", "bread", "milk", "eggs", "butter"]
 
while True:
    print("\n--- Inventory Menu ---")
    print("(a) Add item to end of list")
    print("(b) Insert item at a specific position")
    print("(c) Remove item by name")
    print("(d) View sorted inventory")
    print("(e) Quit")

    choice = input("\nChoose an option: ").strip().lower()


    if choice == "a":
        item = input("Enter item to add: ").strip()
        inventory.append(item)
        print(f'"{item}" added to the end. Current list: {inventory}')

    elif choice == "b":
        item = input("Enter item to insert: ").strip()
        pos = int(input(f"Enter position (0 to {len(inventory)}): "))
        inventory.insert(pos, item)
        print(f'"{item}" inserted at position {pos}. Current list: {inventory}')

    elif choice == "c":
        item = input("Enter item to remove: ").strip()
        if item in inventory:
            inventory.remove(item)
            print(f'"{item}" removed. Current list: {inventory}')
        else:
            print(f'"{item}" not found in inventory.')

    elif choice == "d":
        sorted_inventory = inventory.copy()
        sorted_inventory.sort()
        print(f"Sorted inventory: {sorted_inventory}")

    elif choice == "e":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a-e.")