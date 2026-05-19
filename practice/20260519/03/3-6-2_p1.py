"""
概要
0除算による例外に対処する
処理の流れ
変数num1、変数num2にユーザが入力した値を代入し、変数resultに「0」を代入する
変数num1の値を変数num2の値で割り算した結果を、変数resultに代入する
0除算による例外が発生した場合、「0除算はできません」と表示する
例外の有無にかかわらず、変数resultの値を出力する
"""
num1 = int(input("数値1を入力=>"))
num2 = int(input("数値2を入力=>"))
result = 0

try:
    result = num1 / num2
except ZeroDivisionError as e:
    print("0除算はできません")
finally:
    print("数値1 / 数値2:" + str(result))
