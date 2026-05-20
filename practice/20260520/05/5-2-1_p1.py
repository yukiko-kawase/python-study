"""
概要
テキストファイル内の数値の合計を計算する
処理の流れ
chap5.txtを読み取りモードで開き、1行ずつ読み取る
読み取った行を加算して合計を計算する
読み取った値は文字として識別されているため、数値に変換する必要あり
合計を表示する
"""
total = 0
with open("chap5.txt","r",encoding="utf8") as file:
    for line in file:
        total += int(line)
print(total)
