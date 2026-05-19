"""
概要
数値をリストに格納された複数の値で繰り返し除算する
その際、０除算による例外が発生した場合でも、残りの除算を継続する
処理の流れ
引数2つ受け取り、除算した結果を返すdivide関数を定義する
除算の対象となる変数targetと、除算で使用する数値のリストを格納する変数divsのリストから取り出した要素を1つ渡す
divide関数の戻り値はtargetに代入する
divaide関数でZeroDivisionErrorが発生した場合「0除算はスキップします。」と表示する
変数targetの値を表示する
"""
def divaide(num1,num2):
    return num1 / num2

target = 100
divs = [5,4,1,0,5]

for div in divs:
    try:
        target = divaide(target,div)
    except ZeroDivisionError as e:
        print("0除算はスキップします。")
# Pythonにおける割り算は常に浮動小数点数で結果を返す
print(target)