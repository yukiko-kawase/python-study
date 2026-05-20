# テキストデータと  for文を組み合わせた例
with open("member.txt","r",encoding="utf8") as file:
    for name in file:
        print(name)


# prit関数は表示するデータの後に自動的に改行コードを追加する
# １行ずつprint関数で表示すると、テキストデータ内の1行目2行目の行末に改行コードが含まれる

# 回避方法
# print関数に「end=""」という形でキーワード引数を渡す
# 「end=""」とすることで、print関数の末尾に自動的に追加される改行コードを空文字("")にできる
with open("member.txt","r",encoding="utf8") as file:
    for name in file:
        print(name,end="")
