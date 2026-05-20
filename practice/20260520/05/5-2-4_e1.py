import json

menu = [{"name":"カレー", "price":" 700"},{"name": "ラーメン","price":"680"},
         {"name":"ピザ","price":"750"}]
with open("menu.json", "w", encoding="utf8") as file:
    # 引数に「ensure_ascii=False」の指定がない
    json.dump(menu,file)

