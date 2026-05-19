import datetime
"""
特定の日時をdatetime型のデータで作成したい場合は、datetime.datetime(2027,1,1)のように
年月日を引数に指定する。datetime型同士を引き算することで、経過時間を求めることも可能
経過時間はtimedeltaクラスのデータであり、「days」のようにつなげて記述すると、
経過時間の日数部分の値を取得できる
"""
current_time = datetime.datetime.now()
print(current_time)
new_year = datetime.datetime(2027,1,1)
print(new_year)
diff = new_year - current_time
print(diff.days,"日")
