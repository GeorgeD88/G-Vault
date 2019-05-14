import data_simplifier
import difflib
import tools
import json


class DataObj:

    def __init__(self, category: str):
        self.category = category
        self.fields = {}


# TODO: Child class for each category.


# TODO: Add **kwargs to build().
def build(category: str, *args) -> dict:  # Returns a dictionary of a data object with passed args in their corresponding fields.
    if type(category).__name__ != 'str':  # Confirms that argument is passed is of type string.
        raise TypeError(f'Value from argument category is type {type(category).__name__}, expected str')
    with open('template.json', 'r') as in_file:  # Opens data.json for reading.
        example = json.load(in_file)  # Extracts json data from template.json.
    if len(args) != len(example[category][0]):
        raise ValueError('Length of args needs to match number of fields for category passed')
    aliases = data_simplifier.list_aliases()  # Makes a list of aliases from categories in data.json.
    if category not in aliases:  # Raises error string passed is not an existent alias and shows closest match.
        match = difflib.get_close_matches(category, aliases, 1, 0.75)[0]  # Returns the closest match within the threshold that difflib finds.
        if match is None:
            raise ValueError(f'String passed for argument category doesn\'t exist: no close matches to {category}')
        else:
            raise ValueError(f'String passed for argument category doesn\'t exist: closest match to {category} is {match}')
    data_object = {}  # Defines data_object to be created as an empty dictionary.
    with open('data.json', 'r') as in_file:  # Opens data.json for reading.
        data = json.load(in_file)  # Extracts json data from data.json.
    for field in data[category][0]:  # Defines a key in data_object as None for every available field of the category.
        data_object[field] = None
    for key in data_object:  # Defines every field in data_object as the arg in the corresponding index of the key.
        data_object[key] = args[tools.index_dict(data_object, key, True)]
    return data_object  # Returns the newly built data_object.


def save(category: str) -> None:
    pass  # TODO: Complete


def edit_data_object(category: str):
    pass  # TODO: Complete
