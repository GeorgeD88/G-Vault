from time import sleep
from data_handler import *
from menu import width, fill
import os


file = DataFile('data.json')


# View Option
def view():
    # Title
    print()
    print(' View '.center(width, '-'))
    print()
    sleep(0.5)

    # Info Viewing
    print('What is the name of the security info you want to view?')
    sleep(0.3)
    while True:
        name = input('Name:\t').lstrip().rstrip()
        if name.lower() not in [value.lower() for value in file.name_list()]:  # That means the password info name is already existent.
            print()
            print('Name non existent, input again')
            print()
            sleep(1)
        else:
            break
    print()
    for key, value in file.load_info(name).items():
        print(f'{key.capitalize()}: {value}')
        sleep(0.3)
    print()
    input('Press ENTER to go to menu')


# New Option
def new():
    # Title
    print()
    print(' New '.center(width, '-'))
    print()
    sleep(0.5)

    # Field Filling
    print('Fill in every field as they come, leave blank if needed (name is required)')
    sleep(0.3)
    print()
    new_info = {'name': None, 'email': None, 'password': None, 'notes': None}
    for key in new_info:
        if key == 'name':
            while True:
                value = input(f'{key.capitalize()}:\t').lstrip().rstrip()
                if value.lower() in [name.lower() for name in file.name_list()]:  # That means the password info name is already existent.
                    print()
                    print('Name taken, choose another name')
                    print()
                    sleep(1)
                else:
                    break
        else:
            value = input(f'{key.capitalize()}:\t').lstrip().rstrip()
        new_info[key] = None if value == '' else value

    # Saving New Info
    print()
    print('initializing object...')
    to_save = Data()
    print('converting dictionary to object...')
    to_save.import_dict(new_info)
    print('saving...')
    file.save_info(to_save)


# Edit Option
def edit():
    # Title
    print()
    print(' Edit '.center(width, '-'))
    print()
    sleep(0.5)

    # Info Editing
    print('What is the name of the security info you want to edit?')
    sleep(0.3)
    while True:
        name = input('Password Info to Change:\t').lstrip().rstrip()
        if name.lower() not in [value.lower() for value in file.name_list()]:  # That means the password info name is already existent.
            print()
            print('Name non existent, input again')
            print()
            sleep(1)
        else:
            break
    info = file.load_info(name)
    file.delete_info(name)
    for key in info:
        value = input(f'{key.capitalize()}:\t').lstrip().rstrip()
        if value == '':  # If they inputted nothing then don't edit the value.
            pass
        else:
            info[key] = value

    # Saving New Info
    print()
    print('initializing object...')
    to_save = Data()
    print('converting dictionary to object...')
    to_save.import_dict(info)
    print('saving...')
    file.save_info(to_save)


# Delete Option
def delete():
    # Title
    print()
    print(' Delete '.center(width, '-'))
    print()
    sleep(0.5)

    # Info Deleting
    print('What is the name of the security info you want to delete?')
    sleep(0.3)
    while True:
        name = input('Name:\t').lstrip().rstrip()
        if name.lower() not in [value.lower() for value in file.name_list()]:  # That means the password info name is already existent.
            print()
            print('Name non existent, input again')
            print()
            sleep(1)
        else:
            break
    print()
    print('getting target password info...')
    passw_list = file.password_list()
    for passw in passw_list:  # Goes through all the password infos until it finds the one with the matching name.
        if passw.name.lower() == name.lower():
            print('getting name of password info...')
            found_name = passw.name
            break
    print('deleting info...')
    file.delete_info(found_name)
    print()
    input('Press ENTER to go to menu')


def export():
    # Title
    print()
    print(' Export '.center(width, '-'))
    print()
    sleep(0.5)

    # File Exporting
    print('What is the path and name of the text file to export to? (Default parameters will be used if left blank)')
    sleep(0.3)
    while True:
        path = input('Path:\t').lstrip().rstrip()
        if not os.path.exists(path):  # That means the password info name is already existent.
            print()
            print(f'No such file or path: {path}, input again')
            print()
            sleep(1)
        else:
            break
    file_name = input('File Name:\t')
    print('exporting...')
    if file_name != '':
        file.export(path, file_name)
    else:
        file.export(path)
