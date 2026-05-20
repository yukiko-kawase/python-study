import json

menu = [{"name":"カレー", "price":" 700"},{"name": "ラーメン","price":"680"},
         {"name":"ピザ","price":"750"}]
with open("menu.json", "w", encoding="utf8") as file:
    json.dump(menu,file,ensure_ascii=False)


"""
json形式のファイルに書き込むデータは、辞書を要素とするリストで用意する
また、json.dumpメソッドのキーワード引数ensure_asciiは、ASCIIコードという文字コードを使って書き込むかどうか指示するもの
デフォルトは「True」になっており、書き込むデータに全角文字(日本語文字)が含まれている場合、指定を忘れてしまうとASCIIコードに
変換されてしまい、内容が読み取れなくなってしまう
"""