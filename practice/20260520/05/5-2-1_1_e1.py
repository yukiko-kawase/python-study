# 存在しないファイル名を指定するとエラーになる
file = open("membe.txt", "r",encoding="utf8")
print(file.read())
file.close
