import simplifier as simp
import difflib
import json


# TODO: Add **kwargs to build().
def build(category: str, **kwargs) -> dict:  # Returns a dictionary of a data object with kwargs passed for it's data fields.
    aliases = simp.list_aliases()  # Makes a list of aliases of categories in data.json.
    # vvvvvvvvvvv Assertion code to make sure that the arguments passed are correct (type, string itself, etc.)
    assert type(category).__name__ == 'str', f'Value from argument category is type {type(category).__name__}, expected str'
    match = difflib.get_close_matches(category, aliases, 1, 0.75)[0]  # Returns the closest match that difflib finds within the threshold.
    assert category in aliases, f'String passed for argument category doesn\'t exist: no close matches to {category}' if match is None else f'String passed for argument category doesn\'t exist: closest match to {category} is {match}'
    # ^^^^^^^^^^^
    empty_obj = empty_object(category)  # Makes an empty data object of the category passed.
    data_object = {}  # Defines an empty dictionary as data_object where the newly constructed data object will be saved to.
    with open('data.json', 'r') as in_file:  # Opens data.json for reading.
        data = json.load(in_file)  # Extracts json data from data.json.
    for field in data[category][0]:  # Defines a key in data_object as None for every available field of the category.
        data_object[field] = None
    for key in data_object:  # Defines every field in data_object as the arg in the corresponding index of the key.
        data_object[key] = kwargs[key]
    return data_object  # Returns the newly built data_object.


def empty_object(category: str) -> dict:  # Returns an empty object of the passed category string.
    with open('Reference Data/template.json', 'r') as in_file:
        data = json.load(in_file)
    empty = data[category][0]
    for key in empty:
        if type(empty[key]) in [str, int, float]:
            empty[key] = None
        elif type(empty[key]) is dict:
            empty[key] = {}
            # for nested_key in empty[key]:
            #    empty[key][nested_key] = None
    return empty


def edit_config(key: str, value):
    with open('config.json', 'r') as in_file:
        data = json.load(in_file)
    data[key] = value
    with open('config.json', 'w') as out_file:
        json.dump(data, out_file)


def check_config(key: str or list):
    with open('config.json', 'r') as in_file:
        data = json.load(in_file)
        if type(key) is str:
            return data[key]
        elif type(key) is list:
            path = f'["{key.pop(0)}"]'
            for elem in key:
                path += f'["{elem}"]'
            return exec(f'data{path}')
