"""
概要
２つの数値の小さい数値から大きい数値までの、すべての整数値の値をたす
処理の流れ
変数Xと変数ｙにユーザが入力した値を数値に変換して代入する
変数Xと変数ｙの値を比較して、大きい値を変数biggerに、小さい値を変数smallerに代入する
それ以外の場合は、変数smallerに変数ｘ、変数biggerに変数ｙを代入する
while文を使って、繰り返し処理で、２つの数値の小さい数値から大きい数値まですべえての値を足して合計を求める
合計した結果を表示する
"""
x = int(input("数値1を入力=>"))
y = int(input("須知2を入力=>"))

bigger = 0
smaller = 0
total = 0

if x > y:
    bigger = x
    smaller = y
else:
    bigger = y
    smaller = x

while smaller <= bigger:
    total += smaller
    smaller += 1
print(total)