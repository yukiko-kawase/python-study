"""
概要
5教科分の得点を受け取り、70点以上の教科が3教科以上あればTrueを、3教科未満であれば
Falseを返す関数を定義する
なお、30点未満の教科1つでもあればFalseを返す
処理の流れ
得点のリストを引数scoresとして受け取り、教科数だけ繰り返し処理を行うjudge関数を定義する
5教科の点数をそれぞれユーザに入力させ、その値をリスト格納する
judge関数を、引数に5教科の点数のリストを渡して呼び出し、結果を出力する
judge関数の詳細
変数count0を代入する
引数scoresの値を1つずつ取り出して繰り返し処理を行い、その値が30点未満だった場合、その時点で
Falseを戻り値として返す。70点以上であれば変数countの値を1増やす
変数countの値が3以上であればTrueを返し、3未満であればFalseを返す
"""

def judge(scores):
    count = 0
    for score in scores:
        if score < 30:
            return False
        elif score >= 70:
            count += 1
    
    if count >= 3:
        return True
    else:
        return False

test1 = int(input("テスト１の得点を入力=>"))
test2 = int(input("テスト２の得点を入力=>"))
test3 = int(input("テスト３の得点を入力=>"))
test4 = int(input("テスト４の得点を入力=>"))
test5 = int(input("テスト５の得点を入力=>"))
tests = [test1,test2,test3,test4,test5]
print(judge(tests))



