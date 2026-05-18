# 辞書
# 変数名　= {"キー"：値,"キー":値,}
cake ={"ID":1,"Name":"ブルーベリーカップケーキ","Price":250}
print(cake["Price"])
cake["Price"] = 270
print(cake)
# keysメソッドを「辞書名.keys()」のように実行することで辞書の中のkeyをすべて取得可能
print(cake.keys())
# valuesメソッドを「辞書名.values()」のように実行することで辞書の中の値をすべて取得可能
print(cake.values())
