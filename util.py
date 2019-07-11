import json

def load_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
