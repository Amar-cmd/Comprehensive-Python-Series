#! +---------------+
#! | CONTACT DIARY |
#! +---------------+

contacts = {}


def menu():
    print("\n==== Contact Diary Menu ====")
    print("1. Add Contact")
    print("2. View All Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. View Unique Phone Numbers")
    print("7. Exit")
    print("="*28)


def add_contact():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone: ")

    if len(phone) != 10:
        print("ERROR: Invalid phone number")
        return

    if name in contacts:
        print("Contact already exists")
        return
    else:
        contacts[name] = phone
        print("Contact Added Successfully!")




# {"name": "1234567890"}
def view_contacts():
    if not contacts:
        print("No Contacts Found")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
        print("-"*20)


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("Contact Found")
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact Not Found")


def update_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        contacts[name] = new_phone
        print("Contact Updated Successfully")
    else:
        print("Contact not found!")


def delete_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully")
    else:
        print("Contact not found!")


def view_unique_phones():
    unique = set(contacts.values())

    if not unique:
        print("NO unique Phone Numbers")
        return

    print("\n--- Unique Phone Numbers ---")
    for num in unique:
        print(num)
    print("-"*28)


while True:
    menu()

    choice = input("Enter your choice (1-7): ").strip()

    match choice:
        case "1":
            add_contact()
        case "2":
            view_contacts()
        case "3":
            search_contact()
        case "4":
            update_contact()
        case "5":
            delete_contact()
        case "6":
            view_unique_phones()
        case "7":
            print("Exiting")
            break
        case _:
            print("Invalid Choice. Please Try Again!")
















