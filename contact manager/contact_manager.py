import json

# The file where contacts will be stored
FILENAME = "contacts.json"

def load_contacts_from_file():
    """Loads contacts from the JSON file."""
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or is empty/corrupt, start with an empty list
        return {}

def save_contacts_to_file():
    """Saves the current contacts dictionary to the JSON file."""
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Adds a new contact to the list and saves to file."""
    print("\n--- Add a New Contact ---")
    name = input("Enter contact name: ").title()
    if name in contacts:
        print(f"⚠️ Error: A contact with the name '{name}' already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts_to_file()
    print(f"✅ Success: Contact '{name}' added.")

def view_contacts():
    """Displays all saved contacts."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("Your contact list is empty.")
    else:
        print(f"{'Name':<20} | {'Phone Number':<15} | {'Email Address'}")
        print("-" * 55)
        for name, details in contacts.items():
            print(f"{name:<20} | {details['phone']:<15} | {details['email']}")

def search_contact():
    """Searches for a specific contact by name."""
    print("\n--- Search for a Contact ---")
    name_to_find = input("Enter the name of the contact to search for: ").title()
    if name_to_find in contacts:
        details = contacts[name_to_find]
        print("\n--- Contact Found ---")
        print(f"Name: {name_to_find}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"❌ Error: Contact '{name_to_find}' not found.")

def update_contact():
    """Updates an existing contact's information and saves to file."""
    print("\n--- Update a Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").title()
    if name_to_update in contacts:
        print(f"Updating contact: {name_to_update}. Leave a field blank to keep current information.")
        new_phone = input(f"Enter new phone number (current: {contacts[name_to_update]['phone']}): ")
        new_email = input(f"Enter new email address (current: {contacts[name_to_update]['email']}): ")

        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email
            
        save_contacts_to_file()
        print(f"✅ Success: Contact '{name_to_update}' updated.")
    else:
        print(f"❌ Error: Contact '{name_to_update}' not found.")

def delete_contact():
    """Deletes a contact from the list and saves to file."""
    print("\n--- Delete a Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").title()
    if name_to_delete in contacts:
        confirm = input(f"Are you sure you want to delete {name_to_delete}? (yes/no): ").lower()
        if confirm == 'yes':
            del contacts[name_to_delete]
            save_contacts_to_file()
            print(f"✅ Success: Contact '{name_to_delete}' has been deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"❌ Error: Contact '{name_to_delete}' not found.")

def main():
    """Main function to run the contact list application."""
    global contacts
    contacts = load_contacts_from_file()

    while True:
        print("\n===== Contact List Menu =====")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Goodbye! Your contacts are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()