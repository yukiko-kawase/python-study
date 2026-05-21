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
    

book = Book("Python入門","FOM出版")
# スーパークラスのメソッドを呼び出す
book.disp_title()
# サブクラスのメソッドを呼び出す
book.disp_info()
# サブクラスのメソッドを呼び出す
book.disp_author()

