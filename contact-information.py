def add_contact(contacts):
    Name = input("Enter your name: ")
    Phone = input("Enter your phone number: ")  # keep as string
    Email = input("Enter your email: ")
    Address = input("Enter your address: ")
    new_contact = {'name': Name, 'phone': Phone, 'email': Email, 'address': Address}
    contacts.append(new_contact)
    print(f"Contact {Name} added successfully.")

def view_contact(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    search_term = input("Enter name or phone number to update: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}")
            new_phone = input("Enter new phone number (leave empty to keep the same): ")
            if new_phone:
                contact['phone'] = new_phone
            new_email = input("Enter new email (leave empty to keep the same): ")
            if new_email:
                contact['email'] = new_email
            new_address = input("Enter new address (leave empty to keep the same): ")
            if new_address:
                contact['address'] = new_address
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print(f"Contact {contact['name']} deleted.")
            return
    print("Contact not found.")

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
