"""
概要
リストユーザが入力した値を要素として追加し、繰り返し処理で合計点を求める
処理の流れ
変数countに数値「1」を代入する
変数scoresに空のリストを代入する
無限ループを作る
無限ループ内では、ユーザが入力した値を変数scoresに追加
次の入力を行うかチェックし、行わない場合には、ループから抜ける
変数scoreに入ったテストの得点から合計を求める
合計を表示する
"""

count = 1
total = 0
scores = []
while True:
    score = int(input("テスト" + str(count) + "の得点を入力=>"))
    scores.append(score)
    count += 1
    next = input("次の得点を入力しますか？(y/n) =>")
    while next != "n" and next != "N" and next != "y" and next != "Y" :
        print("y/nで入力してください")
        next = input("次の得点を入力しますか？(y/n) =>")
    if next == "n" or next == "N":
        break
for score in scores:
    total += score
print("合計点：" + str(total))