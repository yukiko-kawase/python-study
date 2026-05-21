class Access:
    def __init__(self, title):
        self.__title = title

    def disp_title(self):
        print(self.__title)


a = Access("アクセス制御")
a.disp_title()