def parse_input(user_input):
    command, *args = user_input.split(' ')
    command = command.strip().lower()
    return command, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except:
        return "Not all details"
    
def change_contact(args, contacts):
    try:
        name, phone = args
        
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not founded"
    except:
        return "Not all details"
    
def show_phone(args, contacts):
    try:
        name = args[0]

        if name in contacts:
            return contacts[name]
        else: 
           return "Contact not founded" 
    except:
        return "Not all details"

def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main() 


    
