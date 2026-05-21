from Employee2 import Employee2

class Se(Employee2):
    def __init__(self, empno, name, dept,lang):
        super().__init__(empno, name, dept)
        self.lang = lang

    def disp_info(self):
        super().disp_info()
        print("使用言語：" + self.lang)

