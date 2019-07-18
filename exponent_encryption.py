import random
import string


maxOrd = 100
minOrd = 10


# Checks if the result of adding these two ordinals will exceed the max ordinal and returns what makes it work.
def loopover(ord1: int, ord2: int, math: str) -> int:
    if math == 'add':
        spill = ord1 + ord2
        if spill not in range(minOrd, maxOrd):
            excess = spill - maxOrd - minOrd if spill > maxOrd else maxOrd - (minOrd + abs(spill))
            return excess
        else:
            return spill
    elif math == 'sub':
        spill = ord1 - ord2
        if spill not in range(minOrd, maxOrd):
            excess = maxOrd - (abs(spill) - (ord1 - minOrd))
            return excess
        else:
            return spill
    else:
        raise ValueError('Fuck')


def flatten(ordinals: list) -> list:
    result = []
    for ord_key in ordinals:
        cut1 = str(ord_key)[:-1]
        cut2 = int(str(ord_key)[-1])
        result.append([chr(int(cut2)) for i in range(int(cut1))])
    return result


def unflatten(flat: list):
    result = []
    for chunk in flat:
        result.append(int(str(len(chunk)) + str(ord(chunk[0]))))
    return result


def get_key(length: int):
    key_ords = [random.choice(range(minOrd, maxOrd)) for i in range(length)]
    return flatten(key_ords)


def encrypt(plaintext: str, key: list = None):
    if key is None:
        key = get_key(len(plaintext))
    key_ords = unflatten(key)
    text_ords = [ord(char) for char in plaintext]
    cipher = [loopover(text_ords[i], key_ords[i], 'add') for i in range(len(text_ords))]
    return key, flatten(cipher)


def decrypt(cipher: list, key: list):
    key_ords = unflatten(key)
    cipher_ords = unflatten(cipher)
    text = [chr(loopover(cipher_ords[i], key_ords[i], 'sub')) for i in range(len(cipher_ords))]
    return text


cipher, key = encrypt('Hello World!')
text = decrypt(cipher, key)
print(key)
print(cipher)
print(text)
