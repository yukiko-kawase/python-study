import xml.etree.ElementTree as ET

"""
xml.tree.ElementTreeモジュールのparseメソッドを使うことで、階層構造を維持した状態でXML形式のデータ読み込めます。
さらに、戻り値で得た値からgetrootメソッドを呼びだすことで、ルート(最上位階層の中身)を取得できる
変数rootには読み込んだタグとその値の組み合わせ情報が入るので、繰り返し処理で1つずつ要素を取り出すと、タグ名と値を取得できる
item.tagにタグ名、item.textにそのタグで挟まれている値が入る
"""

tree = ET.parse("animals.xml")
root = tree.getroot()
for items in root:
    for item in items:
        print(item.tag + ":" + item.text)

