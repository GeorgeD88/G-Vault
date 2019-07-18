import json


# ----- KEY ----- #
# - Sensitive info: "Password info"
# - Data file where info is saved: "Data file"
# - Saving data to a json file: "Dump"
# - Info going into data.json: "Save" (to)
# - Info coming out of data.json or loading the file itself: "Load" (from)
# - Dictionary terms: "Key", "Value", and "Dictionary"
# - Changing data types: "Convert" (from XYZ to XYZ)
# - Converting objects into dictionaries (& vice versa): "Export" and "Import"
# - Adjective of item that is in a list: "Contain"
# - Stuff contained in lists: "Item"


class Data:  # Python object that contains password info over many attributes.

    def __init__(self, name: str = '', email: str = '', password: str = '', notes: str = ''):
        self.name = name
        self.email = email
        self.password = password
        self.notes = notes

    # Exports password info to a dictionary.
    def export_dict(self):
        # Defines each key of the dictionary as its relative value.
        return {'name': self.name, 'email': self.email, 'password': self.password, 'notes': self.notes}

    # Imports password info from a dictionary
    def import_dict(self, data: dict):
        # Redefines each attribute of the object, Data, as the value from the relative key in the argument, data.
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.notes = data['notes']


class DataFile:  # Python object containing only the name of a data file where all password info is stored.

    def __init__(self, file_name: str):
        self.name = file_name

    # Extracts password info from the list of password info in the data file.
    def load_info(self, name: str):
        with open(self.name, 'r') as in_file:
            data = json.load(in_file)  # Defines data as the loaded data file.
        for info in data['passwords']:  # Iterates through the list of password info in the data file.
            if info['name'].lower() == name.lower():  # Returns the targeted password info (identified by name) when found or None if not found.
                return info
        return None

    # Saves password info to the data file.
    def save_info(self, obj: Data):
        dump = obj.export_dict()  # Defines dump as the argument, obj, converted to a dictionary.
        with open(self.name, 'r') as in_file:
            data = json.load(in_file)  # Defines data as the loaded data file.
        data['passwords'].append(dump)  # Appends the argument, obj, to the list of password info in the loaded data file.
        with open(self.name, 'w') as out_file:
            json.dump(data, out_file)  # Dumps the newly edited variable, data, back into the data file.

    def edit_info(self, name: str, key: str, new_value):
        with open(self.name, 'r') as in_file:
            data = json.load(in_file)  # Defines data as the loaded data file.
        index = self.index_info(name)  # Gets the index of the password info to edit.
        data['passwords'][index][key] = new_value  # Redefines the key with the new value.
        with open(self.name, 'w') as out_file:
            json.dump(data, out_file)

    # Deletes password info from the data file.
    def delete_info(self, name: str):
        with open(self.name, 'r') as in_file:
            data = json.load(in_file)  # Defines data as the loaded data file.
        data['passwords'].remove(self.load_info(name))  # Removes the password info, whose name is equal to the argument, name, from the list of password info.
        with open(self.name, 'w') as out_file:
            json.dump(data, out_file)  # Dumps the newly edited variable, data, back into the data file.

    # Returns the index of password info from the list of password info.
    def index_info(self, name: str):
        with open(self.name, 'r') as in_file:
            passwords = json.load(in_file)['passwords']  # Defines passwords as the list of password info from the data file.
        return passwords.index(self.load_info(name))  # Returns the index of the password info in the list of password info.

    # Returns the amount of passwords saved in the data file.
    def password_amount(self):
        with open(self.name, 'r') as in_file:
            passwords = json.load(in_file)['passwords']  # Defines passwords as the list of password info from the data file.
        return len(passwords)  # Returns the length of the list of passwords.

    # Returns a list of all password info as Data object.
    def password_list(self):
        with open(self.name, 'r') as in_file:
            passwords = json.load(in_file)['passwords']  # Defines passwords as the list of password info from the data file.
        passw_objs = []  # Defines passw_objs as an empty list which will hold Data objects.
        for passw in passwords:
            password_object = Data()  # Defines password_object as an empty Data object.
            password_object.import_dict(passw)  # Imports JSON dictionary into a Data object.
            passw_objs.append(password_object)  # Appends the new Data object to the list of Data objects.
        return passw_objs

    # Returns a list of all password info names.
    def name_list(self):
        with open(self.name, 'r') as in_file:
            passwords = json.load(in_file)['passwords']
        names = []
        for passw in passwords:
            names.append(passw['name'])
        return names

    def export(self, file_path: str = '', file_name: str = 'password_export'):
        with open(self.name, 'r') as in_file:
            passwords = json.load(in_file)['passwords']
        to_save = ''
        for passw in passwords:
            name = passw['name']
            email = passw['email']
            password = passw['password']
            notes = passw['notes']
            to_save += f"""Name: {'' if name is None else name}
Email: {'' if email is None else email}
Password: {'' if password is None else password}
Notes: {'' if notes is None else notes}
-----\n"""
        with open(f'{file_path}\\{file_name}.txt', 'w+') as out_file:
            out_file.write(to_save)

    # Returns the value saved under the key "master" in the data file.
    def get_master(self):
        with open(self.name, 'r') as in_file:
            data = json.load(in_file)  # Defines data as the loaded data file.
        return data['master']  # Returns the value under the key "master".

    # Indents the data file and dumps it back.
    def indent(self):
        with open(self.name, 'r') as in_file:
            data = json.load(in_file)  # Defines data as the loaded data file.
        with open(self.name, 'w') as out_file:
            json.dump(data, out_file, indent=2)  # Dumps the indented version of the data file.
