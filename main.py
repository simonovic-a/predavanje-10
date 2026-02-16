from methods import load_file, save_file

data = load_file("data/users.json")
print(data)

data.append({
    "name": "Stefan Nikolic",
    "age": 56,
    "height": 185,
    "gender": "male"
})

save_file("data/users.json", data)