wort_list = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]
contacts = {}


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            error_message = f"Error in {handler.__name__}: {str(e)}"
            print(error_message)
            if isinstance(e, KeyError):
                print("Contact not found.")
                return handler(*args, **kwargs)
            elif isinstance(e, ValueError):
                print("Invalid input.")
                return handler(*args, **kwargs)
            elif isinstance(e, IndexError):
                print("Index out of range.")
                return handler(*args, **kwargs)
            return handler(*args, **kwargs)
    return wrapper


def hello():
    print("How can I help you?")


@input_error
def add():
    name = input("Input name contact: ")
    name = name.title()
    number = input("Input number contact: ")
    number = int(number)
    contacts[name] = number


@input_error
def change():
    name = input("Input name for change: ")
    name = name.title()
    if name not in contacts:
        raise KeyError
    number = input("Input new number: ")
    number = int(number)
    contacts[name] = number


@input_error
def phone():
    name = input("Input name for print: ")
    name = name.title()
    if name not in contacts:
        raise KeyError
    print(f"{name}: {contacts[name]}")


def show_all():
    for name, number in contacts.items():
        print(f"{name}: {number}")


def exit_program():
    print("Good bye!")


if __name__ == "__main__":
    while True:
        press_wort = input("Input command: ")
        press_wort = press_wort.lower()
        if press_wort == "hello":
            hello()
        elif press_wort == "add":
            add()
        elif press_wort == "change":
            change() 
        elif press_wort == "phone":
            phone()
        elif press_wort == "show all":
            show_all()
        elif press_wort in ["good bye", "close", "exit"]:
            exit_program()
            break
        else:
            print("Please choose command: " + ", ".join(wort_list))
