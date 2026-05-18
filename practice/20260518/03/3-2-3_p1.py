"""
変数scoreに3つのテストの得点のリストを代入し、それぞれ表示する
処理の流れ
３つの変数にユーザが入力したテストの得点を代入する
変数scoreに３つの変数リストとして代入する
リストに格納されたテストの得点を１つずつ表示する
"""
score1 = input("テスト1の得点を入力=>")
score2 = input("テスト2の得点を入力=>")
score3 = input("テスト3の得点を入力=>")

score_list = [score1,score2,score3]
print(score_list[0])
print(score_list[1])
print(score_list[2])


