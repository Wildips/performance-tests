import json

# json to dict
json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data['name'])

# dict to json string
data = {
    "name": "Иван",
    "age": 30,
    "is_student": False
}

json_string = json.dumps(data, indent=4)
print(json_string)

# json file to dict
with open('json_example.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

# dict to json file
with open('data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
