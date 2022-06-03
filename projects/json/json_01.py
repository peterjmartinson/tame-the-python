# serialization = encoding = writing
# deserialization = decoding = reading



import json
# json.dump(data, output_file)  #<<<# writes a Python object to a JSON file as a string
# json.load(input_file)         #<<<# Reads a JSON string from input_file, and returns an associated Python object (like a dict or list)
# json.dumps(data)              #<<<# writes Python object to a Python string
# json.loads(json_string)       #<<<# Reads a json_string and returns an associated Python object


data = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'male',
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H', # This is the seventh son
         'gender': 'male',
         'children':[
            {'name': 'I',
             'gender': 'male',
             'children': []},
            {'name': 'J',
             'gender': 'male',
             'children': []},
            {'name': 'K',
             'gender': 'male',
             'children': []},
            {'name': 'L',
             'gender': 'male',
             'children': []},
            {'name': 'M',
             'gender': 'male',
             'children': []},
            {'name': 'N',
             'gender': 'male',
             'children': []},
            {'name': 'O', # This is the sventh son of the seventh son
             'gender': 'male',
             'children': []}
         ]}
    ]
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_data = json.dumps(data, indent=4)
# print(type(json_data))
# print(json_data)


data_from_file = None
with open("data_file.json", "r") as read_file:
    data_from_file = json.load(read_file)

print(type(data_from_file))
