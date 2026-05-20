"""
概要
employeeクラスを作成する
処理の流れ
Employeeクラスを定義して、従業員番号、氏名、部署名を入力させる
入力した値をもとにEmployeeクラスのオブジェクトを生成し、その情報をメソッドで表示する
Employeeクラスの詳細
インスタンス変数に、従業員番号を表すempno,氏名を表すname,部署名を表すdeptを持つ
__init__メソッドでインスタンス変数のempno,name,deptを設定する
disp_infoメソッドで従業員番号、氏名、部署名を表示する
"""

class Employee:
    def __init__(self,empno, name, dept):
        self.empno = empno
        self.name = name
        self.dept = dept

    def disp_info(self):
        print("従業員番号：" + self.empno)
        print("氏名：" + self.name)
        print("部署名：" + self.dept)