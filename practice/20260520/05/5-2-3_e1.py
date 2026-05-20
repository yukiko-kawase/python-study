import json

with open("animals.json", "r" ,encoding="utf8") as file:
    animals = json.load(file)
# jsonで使われていないキー名を指定すると、エラーになる正しくは、animals["animals"]
for animal in animals["animal"]:
    print(animal)
    print(animal["name"])
