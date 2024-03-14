contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Contact {name} added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if not contacts:
        print("No contacts in the book.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
