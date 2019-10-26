import handler
from time import time, sleep


def line(width: int, line_char: str = '-'):
    line_str = ''
    for i in range(width):
        line_str += line_char
    return line_str


# Application Title
print()
print('G-Vault'.center(100))
sleep(0.2)
print(line(9, '#').center(100))
sleep(0.1)

# Setup Decision
if handler.check_config('new_user'):  # If the user is a new user.
    print('Let\'s set up G-Vault')
    sleep(0.25)
    print('First, some basic personal info')
    sleep(0.2)
    fname = input('First Name: ')
    lname = input('Last Name: ')
    print('Now we\'re gonna need some security info')
    sleep(0.2)
    password = input('Master Password: ')
    email = input('Email (for recover and authentication): ')
    print('saving new information:')
    sleep(0.15)
    with open('config.json', 'w+') as out_file:
        jso

# Security/Login
accessGranted = False
while not accessGranted:
    input()
