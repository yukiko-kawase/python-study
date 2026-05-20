"""
概要
テキストファイルに数値を書き込む
処理の流れ
chap5.txtを追記モードで開く
開いたファイルに「\n6\n7」を書き込む
"""
with open("chap5.txt", "a" ,encoding="utf8") as file:
    file.write("\n6\n7")