class Employee3:
    def __init__(self,empno, name, dept):
        self.__empno = empno
        self.__name = name
        self.__dept = dept

    def disp_info(self):
        print("従業員番号：" + self.__empno)
        print("従業員名：" + self.__name)
        print("部署名：" + self.__dept)
    
    def chg_dept(self):
        dept = input("従業員番号" + self.__empno + "新しい部署名は？=>")
        self.__dept = dept
