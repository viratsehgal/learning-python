names = []
phones = []

while True:
    print("\n--- Contact Manager ---")
    print("a) Add a contact")
    print("b) Search for a contact")
    print("c) Delete a contact")
    print("d) View all contacts")
    print("e) Quit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        names.append(name)
        phones.append(phone)
        print(f"Contact '{name}' added.")

    elif choice == 'b':
        name = input("Enter name to search: ")
        if name in names:
            i = names.index(name)
            print(f"Name: {names[i]}, Phone: {phones[i]}")
        else:
            print("Contact not found.")

    elif choice == 'c':
        name = input("Enter name to delete: ")
        if name in names:
            i = names.index(name)
            names.remove(names[i])
            phones.pop(i)
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")

    elif choice == 'd':
        if names:
            print("\nAll Contacts:")
            for i in range(len(names)):
                print(f"  {names[i]} - {phones[i]}")
        else:
            print("No contacts saved.")

    elif choice == 'e':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
