"""
概要
JSON 形式のファイルを読み取り、格納されているデータの価格(Price)の合計を表示する
処理の流れ
JSON 形式のファイルの読み込みに必要な標準モジュールを読み込む
cake.jsonを開く
開いたデータの価格(Price)を加算する。なお、データは文字として扱われる為、加算するためには
数値に変換する必要がある
合計価格を表示する
"""
import json

with open("cake.json", "r" ,encoding="utf8") as file:
    cakes = json.load(file)
total = 0
for cake in cakes:
    total = total + int(cake["Price"])
print(total)