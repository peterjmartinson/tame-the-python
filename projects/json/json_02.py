# calls fake JSON from
# https://jsonplaceholder.typicode.com/

import requests
import json

def get_json(resource='todos', index=None):
    uri = 'https://jsonplaceholder.typicode.com'
    uri += '/' + resource
    if index:
        uri += '/' + str(index)
    data = requests.get(uri)
    return data

if __name__ == "__main__":
    data = get_json(resource='posts')
    data_json = data.json()
    data_text = data.text
    print('data_json type: ', type(data_json))
    print('data_text type: ', type(data_text))
    for key, value in data_json[0].items():
        print(f'{key}\t: {value}')
