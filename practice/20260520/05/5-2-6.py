import xml.etree.ElementTree as ET
# itemsタグの情報を作る
root = ET.Element("items")
# itemタグの情報を作る
item = ET.Element("item")
# itemsタグの中にitemタグを入れる
root.append(item)
# 「<タグ>値</タグ>」の情報を作るにはET.SubElementメソッドを使う
# 親にしたい要素が入った変数と、タグの名前を引数にする
val1 = ET.SubElement(item,"name")
# nameタグで挟む値を設定
val1.text = "はじめてのPython"
val2 = ET.SubElement(item,"price")
val2.text = "1980"
# ET.ElementメソッドでXML形式のデータを作る
tree = ET.ElementTree(root)
# writeメソッドでファイル「book.xml」に文字コードutf8で書き込み
tree.write("book.xml", encoding="utf8")
