wort_list = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]
contacts = {"Wowa": 777}
a = None
b = None


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            error_message = f"Error in {handler.__name__}: {str(e)}"
            print(error_message)
            if isinstance(e, KeyError):
                print("Contact not found.")
                rename()
                return enter()
            elif isinstance(e, ValueError):
                print("Invalid input.")
                rename()
                return enter()
            elif isinstance(e, IndexError):
                print("Index out of range.")
                rename()
                return enter()
            rename()
            return enter()
    return wrapper


def hello():
    print("How can I help you?")
    rename()


@input_error
def add(name):
    key_value = name.title()
    if key_value.isdigit():
        raise ValueError
    elif key_value.isalpha():
        raise ValueError
    key_value = name.split()
    name = key_value[0].title()
    number = int(key_value[1])
    contacts[name] = number
    rename()


@input_error
def change(name):
    key_value = name.title()
    if key_value.isdigit():
        raise ValueError
    elif key_value.isalpha():
        raise ValueError
    key_value = key_value.split()
    name = key_value[0].title()
    number = int(key_value[1])
    if name not in contacts:
        raise KeyError
    contacts[name] = number
    rename()


@input_error
def phone(name):
    if name.isdigit():
        raise KeyError
    if name.isalpha():
        name = name.title()
        if name not in contacts:
            raise KeyError
        print(f"{name}: {contacts[name]}")
        rename()
    else:
        raise KeyError


def show_all():
    for name, number in contacts.items():
        print(f"{name}: {number}")
    rename()
        

def exit_program():
    print("Good bye!")
    

def check(wort):
        if wort == "hello":
            hello()
        elif wort == "add":
            add(b)
        elif wort == "change":
            change(b)
        elif wort == "phone":
            phone(b)
        elif wort == "show all":
            show_all()
        elif wort in ["good bye", "close", "exit"]:
            return exit_program()
        else:
            print("Please choose a valid command: " + ", ".join(wort_list))
            rename()
        

def rename():
    global a, b
    a = b = None


def enter():
    while True:
        command = input("Input command: ").lower()
        global a, b
        for i in wort_list:
            if command == i:
                if command in ["add", "change", "phone"]:
                    a = command
                    print(f"Enter text for command: {command}")
                    enter()
                    break
                elif command == i:
                    a = command
                    check(a)
                    break 
            if a is None:
                i = None
            if a is not None:
                b = command
                check(a)
                break   
        if command not in wort_list and i is None:
            print("Please choose a valid command: " + ", ".join(wort_list))
            enter()
        if a in ["good bye", "close", "exit"]:
            break

    
if __name__ == "__main__":
    enter()
