from time import time, sleep
from datetime import date
from data_handler import *


def get_date() -> str:
    return date.today().strftime('%m/%d/%Y')


width = 25
fill = '='
file = DataFile('data.json')
startTime = time()  # Start time of session.


def run_menu():
    # Title
    print()
    print(' G-Vault '.center(width, fill))
    print()
    sleep(0.5)
    print(get_date().center(width, ' '))
    print()
    sleep(0.5)

    # Security
    curr_master = DataFile('data.json').get_master()
    while True:  # Keeps asking for input until it matches the master password stored in data.json.
        master = input('Master Password:\t').lstrip().rstrip()  # Defines master as a left and right stripped string input.
        if master == curr_master:
            break  # Breaks loop if the password matches the master password in data.json.
        else:
            print()
            print('Incorrect Password, try again')
            print()
