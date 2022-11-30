from collections import OrderedDict
import json


# 1. ================= DASAR
person = OrderedDict()
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": [
        "engineer",
        "programmer"
    ]
}

# ========= SERIALIZE/ENCODE KE JSON
person_json = json.dumps(person, indent=4)
print(person_json)
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# ========= DESERIALIZE/DECODE DARI DATA JSON
person_decode = json.loads(person_json)
print(person_decode)
with open('person.json', 'r') as file:
    person_decode_file = json.load(file)
    print(person_decode_file)


# 2. ================= DASAR
person_2 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": [
        "engineer",
        "programmer"
    ]
}


# ========= SERIALIZE/ENCODE KE JSON
# dengan penggunaan sort_keys=True
# output json akan ascending berdasarkan keys alphabet
person_json_2 = json.dumps(person_2, indent=4, sort_keys=True)
print(person_json_2)
with open('person_2.json', 'w') as file:
    json.dump(person_2, file, indent=4, sort_keys=True)


# ========= DESERIALIZE/DECODE DARI DATA JSON
person_2_decode_json = json.loads(person_json_2)
print(person_2_decode_json)

with open('person_2.json', 'r') as file:
    person_2_decode_json_file = json.load(file)
    print(person_2_decode_json_file)
