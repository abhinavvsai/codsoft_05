import json

contacts = []

def save_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")

def search_contacts():
    term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if term in contact['name'] or term in contact['phone']]
    if found_contacts:
        for contact in found_contacts:
            print_contact(contact)
    else:
        print("No contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("1. Update phone number")
            print("2. Update email")
            print("3. Update address")
            choice = input("Enter your choice: ")
            if choice == '1':
                contact['phone'] = input("Enter new phone number: ")
            elif choice == '2':
                contact['email'] = input("Enter new email: ")
            elif choice == '3':
                contact['address'] = input("Enter new address: ")
            else:
                print("Invalid choice")
                return
            save_contacts()
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def print_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")
    print("-" * 20)

def main():
    load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
