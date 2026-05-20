# open(ファイルパス,"モード(読み取り専用など)",encoding="文字コード")
file = open("member.txt","r",encoding="utf8")
print(file.read())
file.close