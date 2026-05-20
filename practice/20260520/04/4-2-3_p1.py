"""
概要
外部のAPIにアクセスして、郵便番号に対する住所を取得し表示する
(利用APIの詳細：ユーザが入力した郵便番号)に対して、GETメソッドによる呼び出しを行う
取得したJSONから、すべての住所のデータを辞書型として取得する
辞書型のデータを加工し、「市や区の名前」と「町や丁目の名前」の値はキー「town」から取得できる
"""

import requests

postal_code = input("検索したい地域の郵便番号(-なし)を入力してください=>")
url = "https://geoapi.heartrails.com/api/json?method=searchByPostal&postal=" + postal_code

response = requests.get(url)
locations = response.json()["response"].get("location")

if locations != None:
    for location in locations:
        print(location["city"] + location["town"])
else:
    print("住所が見つかりません")
     

