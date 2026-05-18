# Input関数
# yearなど数値に変換できない文字列を入力した場合、エラーとなる
seireki = int(input("西暦を入力=>"))
reiwa = seireki - 2018
print("令和" + str(reiwa) + "年")
