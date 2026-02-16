
import json

with open("data.json", "r") as file:
    data = json.load(file)

    print(data)

    data.append({
        "name": "Sara Veljkovic",
        "age": 22,
        "height": 155,
        "gender": "female"

    })


print(data)


with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)
