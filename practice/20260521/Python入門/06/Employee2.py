class Employee2:
    def __init__(self,empno, name, dept):
        self.empno = empno
        self.name = name
        self.dept = dept

    def disp_info(self):
        print("従業員番号：" + self.empno)
        print("従業員名：" + self.name)
        print("部署名：" + self.dept)
    
    def chg_dept(self):
        dept = input("従業員番号" + self.empno + "新しい部署名は？=>")
        self.dept = dept
