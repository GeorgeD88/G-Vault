import time


def line(width: int, line_char: str = '-'):
    line_str = ''
    for i in range(width):
        line_str += line_char
    return line_str


print('Welcome to G-Vault!'.center(150))
time.sleep(0.5)
print()
time.sleep(0.5)
print('The one stop shop password manager to store your account information, credit cards, passwords, and more!'.center(150))
time.sleep(1)
print('\n', line(150, '#'))
