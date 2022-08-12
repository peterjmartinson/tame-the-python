# calls fake JSON from
# https://jsonplaceholder.typicode.com/

import requests
import json

def get_response(resource="todos", index=None):
    uri = "https://jsonplaceholder.typicode.com"
    uri += "/" + resource
    if index:
        uri += "/" + str(index)
    data = requests.get(uri)
    return data

def response_to_object_requests(data):
    return data.json()

def response_to_object_json(data):
    return json.loads(data.text)


if __name__ == "__main__":
    data = get_response(resource="posts")
    data_json = data.json() # returns Python object
    data_text = data.text   # returns string
    print("data.json() type: ", type(data_json))
    print("data.text type: ", type(data_text))
    for key, value in data_json[0].items():
        print(f"{key}\t: {value}")
        

    print("%%%%%%%%%%%%%%%%%%%%")
    from_requests = response_to_object_requests(data)
    from_json     = response_to_object_json(data)
    print("data.json(): ", type(from_requests))
    print("json.loads(data.text): ", type(from_json))


    # print(data.text)

