# with文を使うと内部で自動的にcloseメソッドが呼び出され、ファイルが閉じられる
with open("member.txt","r",encoding="utf8") as file:
    print(file.read())