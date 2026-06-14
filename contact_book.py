contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("\nContact Added Successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found!")
        return
        
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact():
    key = input("Enter name or phone: ")
    found = False
    
    for name, info in contacts.items():
        if key == name or key == info['phone']:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
            break
    
    if not found:
        print("\nNo matching contact found.")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        print("Leave blank if no change.")
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")
        
        if phone:
            contacts[name]['mobile'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
            
        print("\nContact Updated!")
    else:
        print("\nContact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        contacts.pop(name)
        print("\nContact Deleted!")
    else:
        print("\nAlready removed or not found!")
contacts = {}

def contact_book():
    while True:
        print("\n--- Contact Book App ---")
        print("1. Create Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Count Contact")
        print("7. Exit")

        choice = input("Enter your choice = ")

        if choice == "1":
            name = input("Enter name = ")
            if name in contacts:
                print("Contact already exists!")
            else:
                age = input("Enter age = ")
                email = input("Enter email = ")
                mobile = input("Enter mobile = ")
                contacts[name] = {"age": age, "email": email, "mobile": mobile}
                print("Contact added successfully!")

        elif choice == "2":
            name = input("Enter name to view = ")
            if name in contacts:
                print(contacts[name])
            else:
                print("Contact not found!")
        elif choice == "3":
            name = input("Enter name to update = ")
            if name in contacts:
                age = input("Enter new age = ")
                email = input("Enter new email = ")
                mobile = input("Enter new mobile = ")
                contacts[name] = {"age": age, "email": email, "mobile": mobile}
                print("Contact updated!")
            else:
                print("Contact not found!")
        elif choice == "4":
            name = input("Enter name to delete = ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted!")
            else:
                print("Contact not found!")
        elif choice == "5":
            search_name = input("Search name = ")
            found = False
            for n, c in contacts.items():
                if search_name.lower() in n.lower():
                    print(n, c)
                    found = True
            if not found:
                print("No contact found!")
        elif choice == "6":
            print("Total contacts =", len(contacts))
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
contact_book()
