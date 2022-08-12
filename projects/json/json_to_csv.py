
import requests
import json
import csv

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

def list_of_dicts_to_json(json_list, output_file="test.csv"):
    with open(output_file, "w") as csvfile:
        json_writer = csv.writer(csvfile, delimiter=",", quotechar='"', lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        json_writer.writerow(json_list[0].keys())
        for row in json_list:
            json_writer.writerow(row.values())
    return True

if __name__ == '__main__':
    data = get_response(resource="posts")
    json_list = response_to_object_json(data)
    list_of_dicts_to_json(json_list)
    
