from menu import width, fill, run_menu
from data_handler import *
from time import sleep
import choices


file = DataFile('data.json')

run_menu()

while True:
    # Title
    print()
    print(' G-Vault '.center(width, fill))
    print()
    sleep(0.5)

    # Choice Selection
    options = ['VIEW', 'LIST', 'NEW', 'EDIT', 'DELETE', 'EXPORT']
    if file.password_amount() == 0:  # If there are no existing passwords.
        for i in range(2, len(options)-1):
            print(f'[{i-1}] {options[i]}')
            sleep(0.25)
        print()
        print(' [QUIT]')
        sleep(0.2)
        print()
        while True:
            while True:
                choice = input('Choice:\t').lstrip().rstrip()  # Defines choice as the user's input for what to do next.
                if choice.lower() == 'quit':
                    break
                else:  # Other than being "quit".
                    try:  # Integer handling.
                        choice = int(choice)
                        if choice not in [num for num in range(1, len(options)-1)]:  # If choice was out of range.
                            print()
                            print('Choice out of range, pick again')
                            sleep(1)
                            print()
                        else:
                            break
                    except ValueError:  # String handling.
                        print()
                        print('Invalid choice, pick again')
                        sleep(1)
                        print()
            if type(choice) is int or choice.lower() == 'quit':
                if choice == 1:
                    choices.new()
                    break
                elif choice == 2:
                    choices.edit()
                    break
                elif choice == 3:
                    choices.delete()
                    break
                elif choice.lower() == 'quit':
                    quit()
            else:
                print()
                print('Invalid Choice, pick again')
                print()
    else:  # Else, there are existing passwords.
        for i in range(len(options)):
            print(f'[{i + 1}] {options[i]}')
            sleep(0.25)
        print()
        print(' [QUIT]')
        sleep(0.2)
        print()
        while True:
            while True:
                choice = input('Choice:\t').lstrip().rstrip()  # Defines choice as the user's input for what to do next.
                if choice.lower() == 'quit':
                    break
                else:  # Other than being "quit".
                    try:  # Integer handling.
                        choice = int(choice)
                        if choice not in [num + 1 for num in range(len(options))]:  # If choice was out of range.
                            print()
                            print('Choice out of range, pick again')
                            sleep(1)
                            print()
                        else:
                            break
                    except ValueError:  # String handling.
                        print()
                        print('Invalid choice, pick again')
                        sleep(1)
                        print()
            if type(choice) is int or choice.lower() == 'quit':
                if choice == 1:
                    choices.view()
                    break
                elif choice == 2:
                    choices.list_view()
                elif choice == 3:
                    choices.new()
                    break
                elif choice == 4:
                    choices.edit()
                    break
                elif choice == 5:
                    choices.delete()
                    break
                elif choice == 6:
                    choices.export()
                    break
                elif choice.lower() == 'quit':
                    quit()
            else:
                print()
                print('Invalid Choice, pick again')
                print()
