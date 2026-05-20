import json

with open("animals.json", "r", encoding="utf8") as file:
    animals = json.load(file)
for animal in animals["animals"]:
    print(animal)
    print(animal["name"])

    """
    変数animals["animals"]には辞書を要素とするリストが入っている為、for文のデータ群として利用できる
    5行目のfor文で変数animalにはリストの中の辞書の要素が代入される為、キーを指定すると組み合わせの値を取得できる
    """