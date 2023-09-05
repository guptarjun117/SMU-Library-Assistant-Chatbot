import json


with open('libfaq_cleaned.json', 'r') as json_file:
    for line in json_file:
        data = json.loads(line)
        print(line)

        for key,value in data.items():
            print(key, value)