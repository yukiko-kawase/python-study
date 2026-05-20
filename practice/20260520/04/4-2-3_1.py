# 郵便番号を指定してアクセスすると、該当する住所を取得できるWebAPIを使用する
# requestモジュールをインポートする
import requests

# 変数urlに文字列"https://geoapi.heartrails.com/api/json?method=searchByPostal&postal=1440054"を代入する
url = "https://geoapi.heartrails.com/api/json?method=searchByPostal&postal=1440054"

# 変数urlに対してGETメソッドによる呼び出しを実行し、結果を変数responseに代入する
response = requests.get(url)

# 変数respomseのデータのJSONを取得し、その中のキー「response」の中のキー「location」のデータを表示する
print(response.json()["response"]["location"])