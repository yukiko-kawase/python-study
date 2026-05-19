"""
概要
入力した整数を5乗した数値を、繰り返し処理を利用して計算し、結果を表示する
処理の流れ
変数numにユーザが入力した値を数値に変換して代入する
変数resultに数値[1]を代入する
変数resultの値に変数numの値をかけた結果を変数resultに代入する処理をfor文を使って5回繰り返す
5回繰り返した後、変数resultの値を表示する
"""
num = int(input("整数を入力=>"))
result = 1
for i in range(5):
    result *= num
print("5乗した結果：" + str(result))
