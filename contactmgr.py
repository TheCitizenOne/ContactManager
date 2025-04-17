# Contact Manager by The_Citizen
contacts = {}

def add_contact(name, number, email):
    contacts[name] = number, email

def list_contacts():
    if not contacts:
        print("-- Contact list is empty. --\n")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"- {name}: {number}")
            print()

def find_contact(name):
    res = contacts.get(name)
    if res == None:
        print(f"There's no such contact named as {name}\n")
    else:
        print(f"- {name}: {res}\n")

def del_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted.\n")
    else:
        print(f"There is no such contact named as {name}\n")
    
def display():
    print("Welcome to the Contact Manager.")
    print("--------------------------")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Find contact")
    print("4. Remove contact")
    print("5. Exit")

def main():
    while True:
        display()
        opt = input("Select an option [1-5]: ")

        if opt == "1":
            x = input("Enter the name of new contact: ")
            if x in contacts:
                print("Contact exists.\n")
            else:
                y = input("Enter the number of new contact: ")
                z = input("Enter the email of new contact: ")
                add_contact(x, y, z)
                print("Contact is added.\n")
        elif opt == "2":
            list_contacts()
        elif opt == "3":
            x = input("Enter the name of contact: ")
            find_contact(x)
        elif opt == "4":
            x = input("Enter the name of contact: ")
            del_contact(x)
        elif opt == "5":
            exit()
        else:
            print("Enter a valid number.\n")

if __name__== "__main__":
    main()
