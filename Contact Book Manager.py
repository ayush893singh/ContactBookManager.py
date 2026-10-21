import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    contacts[name] = phone
    save_contacts(contacts)
    print("Contact saved successfully!")


def view_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return

    print("\n---------- ALL CONTACTS ----------")
    for name, phone in contacts.items():
        print(f"Name: {name} | Phone: {phone}")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    for contact_name, phone in contacts.items():
        if contact_name.lower() == name.lower():
            print(f"Name: {contact_name}")
            print(f"Phone: {phone}")
            return

    print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()

    for contact_name in contacts:
        if contact_name.lower() == name.lower():
            phone = input("Enter new phone number: ").strip()

            if not phone:
                print("Phone number cannot be empty.")
                return

            contacts[contact_name] = phone
            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    for contact_name in list(contacts):
        if contact_name.lower() == name.lower():
            del contacts[contact_name]
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


contacts = load_contacts()

while True:
    print("\n========================================")
    print("         CONTACT BOOK MANAGER")
    print("========================================")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("========================================")

    choice = input("Choose option: ").strip()

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("Thank you for using Contact Book Manager!")
        break

    else:
        print("Invalid choice. Please select 1 to 6.")