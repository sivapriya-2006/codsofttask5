import os

contacts = {}

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    # Function to add a new contact
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added successfully.")

def view_contact_list():
    # Function to display a list of all contacts
    if not contacts:
        print("No contacts found.")
        return

    print("Contact List:")
    for name, contact_info in contacts.items():
        print(f"Name: {name}, Phone: {contact_info['phone']}")

def search_contact():
    # Function to search for a contact by name or phone number
    query = input("Enter the contact name or phone number to search: ")
    
    results = []
    for name, contact_info in contacts.items():
        if query.lower() in name.lower() or query in contact_info['phone']:
            results.append((name, contact_info))

    if not results:
        print("No matching contacts found.")
        return

    print("Matching Contacts:")
    for name, contact_info in results:
        print(f"Name: {name}, Phone: {contact_info['phone']}, Email: {contact_info['email']}, Address: {contact_info['address']}")

def update_contact():
    # Function to update contact details
    name = input("Enter the name of the contact to update: ")

    if name not in contacts:
        print("Contact not found.")
        return

    print("Current Contact Information:")
    print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")

    # Prompt user for updated information
    phone = input("Enter the new phone number (press Enter to keep current): ") or contacts[name]['phone']
    email = input("Enter the new email address (press Enter to keep current): ") or contacts[name]['email']
    address = input("Enter the new address (press Enter to keep current): ") or contacts[name]['address']

    # Update contact details
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact updated successfully.")

def delete_contact():
    # Function to delete a contact
    name = input("Enter the name of the contact to delete: ")

    if name not in contacts:
        print("Contact not found.")
        return

    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")

def main():
    while True:
        clear_screen()
        print("Contact Book Application")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to continue.")

if __name__ == "__main__":
    main()

