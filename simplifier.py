from uszipcode import SearchEngine
import json


def info_from_zip(zipcode: str, *args) -> dict:  # Uses uszipcode library to return requested info about zip code.
    search = SearchEngine(simple_zipcode=True)
    info_dict = search.by_zipcode(zipcode).to_dict()
    return_dict = {}
    for arg in args:
        try:
            return_dict[arg] = info_dict[arg]
        except KeyError:
            continue
    return return_dict


def abbreviator(original: str) -> str:  # Returns the abbreviation of the word passed for argument original.
    abbrev = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    was_left = False
    was_center = False
    was_right = False
    start_w_vowel = False
    # Example: accounts => left[acc] center[ou] right[nts] | documents => left[d] center[o] right[cuments]
    iteration = 0
    for ch in original:
        is_vowel = True if ch in vowels else False
        iteration += 1
        if iteration == 1:
            was_left = True
            start_w_vowel = True if is_vowel else False
        # Everything below here (after the continue statement) is only for all letters after the first letter.
        elif start_w_vowel:  # If the word starts with a vowel: V|C|REST => V|C
            if not is_vowel and was_left:
                was_left = False
                was_center = True
            elif is_vowel and was_center and not was_left:
                break
        else:  # Else: C|V|C => C|V|c
            if is_vowel and was_left:
                was_left = False
                was_center = True
            elif not is_vowel and was_center:
                was_center = False
                was_right = True
            elif is_vowel and was_right:
                break
        abbrev += ch
    return abbrev


def plural2singular(plural: str) -> str:  # Returns singular of plural word (is a function because has to mess with "ses" and "s" endings).
    return plural[:-2] if plural[-3:] == 'ses' else plural[:-1]


def data_checker(value, confirm_type: str or object):
    if type(value).__name__ != str(confirm_type):  # Confirms that the argument is passed is of type, confirm_type.
        raise TypeError(f'Value from argument category is type {type(value).__name__}, expected {confirm_type}')


def is_container(value, return_type: bool = False) -> type or None:
    for container in [dict, list, tuple]:  # For every type of container.
        if data_checker(value, container):  # If the data type of the value is equal to the current iteration of the containers.
            return True if not return_type else type(value)  # Return True if they don't want the data type itself to be returned.
    return False  # If none of the containers match, continue through the function and return False.


def index_dict(dictionary: dict, element, is_key: bool) -> int:  # Returns index of a key or value in dictionary because there is no default dict method for it.
    if is_key is True:
        elems: list = list(dictionary.keys())
    elif is_key is False:
        elems: list = list(dictionary.values())
    else:
        raise TypeError(f'Value from argument is_key is type {type(is_key).__name__}, expected bool')
    return elems.index(element)


def dict_aliases() -> dict:  # Returns a dictionary of the aliases of categories in data.json.
    with open('data.json', 'r') as in_file:
        data = json.load(in_file)
        data_types = [key for key in data]
    aliases = {}
    for cat in data_types:
        abbrev = abbreviator(cat)
        aliases[cat] = [cat[:1], abbrev, abbrev + ('es' if abbrev[-1] == 's' else 's'), plural2singular(cat), cat]  # Get aliases from root category name.
    return aliases


def list_categories() -> list:  # Returns a list of the categories in data.json.
    with open('data.json', 'r') as in_file:
        data = json.load(in_file)
    return [cat for cat in data]


def list_aliases() -> list:  # Returns a list of the aliases of the categories in data.json.
    with open('data.json', 'r') as in_file:
        data = json.load(in_file)
    alias_lists = []
    for cat in list_categories():
        abbrev = abbreviator(cat)
        alias_lists.append([cat[:1], abbrev, abbrev + ('es' if abbrev[-1] == 's' else 's'), plural2singular(cat), cat])
    aliases = []
    for a_list in alias_lists:
        for alias in a_list:
            aliases.append(alias)
    return aliases


def simplify(string: str, return_lowercase: bool = True) -> str:  # Removes white space on edges and changes case.
    stripped = string.rstrip().lstrip().replace(' ', '')  # Removes all white space.
    return stripped.lower() if return_lowercase else (stripped.upper() if not return_lowercase else stripped)
