# 変数scoreにユーザが入力したい値をリストで代入し、繰り返し処理で合計点を計算する
"""
処理の流れ
３つの変数にユーザが入力したテストの得点を代入する
入力された３つの値を要素とするリストを作り、変数scoreに代入する
for文を使った繰り返し処理で、変数scoreの要素から合計を求める
繰り返し処理が終わった後、合計を表示する
"""
score1 = int(input("テスト1の得点=>"))
score2 = int(input("テスト2の得点=>"))
score3 = int(input("テスト3の得点=>"))
scores = {score1,score2,score3}
total = 0
for score in scores:
    total += score
print("合計点：" + str(total))
