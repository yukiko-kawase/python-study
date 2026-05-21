class Rent:
    def __init__(self,title):
        self.title = title
    
    def disp_title(self):
        print("【Rent】タイトル:" + self.title)

    def disp_info(self):
        print("【Rent】の内容です")


class Book(Rent):
    def __init__(self, title, author):
        # サブクラスからスーパークラスのメソッドを呼び出す
        super().__init__(title)
        self.author =author

    def disp_info(self):
        print("【Book】本の内容です")

    def disp_author(self):
        print("【Book】著者名：" + self.author)
    
# 引数が足りない
book = Book("Python入門")
# スーパークラスのメソッドを呼び出す
book.disp_title()
# サブクラスのメソッドを呼び出す
book.disp_info()
# サブクラスのメソッドを呼び出す
book.disp_author()

"""
エラーの発生場所：24行目book = Book("Python入門")
エラーの意味：引数authorに渡される値が設定されていない
対処法：引数authorに渡す値を指定する(オーバーライドしたメソッドに定義された数の引数を渡す必要がある)
"""

