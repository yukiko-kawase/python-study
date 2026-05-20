# open関数で得た値をそのままprint関数の引数にしても、テキストファイルの内容は表示されません
# テキストファイルに関する情報が表示される
file = open("member.txt","r",encoding="utf8")
print(file)
file.close

"""
open関数の戻り値をprint関数に渡すと、テキストファイルに関する情報が表示される
モードに「r」を指定して開いたテキストデータは、io.TextIOWrapper型というデータ型に格納する
開いたテキストファイルの内容を取得するには、io.TextIOWrapper型の値からreadメソッドを呼び出す必要がある
"""
