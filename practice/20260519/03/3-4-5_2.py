age = ""
while True:
    age = input("年齢を入力してください=>")
    # 変数ageの値が全て数字の場合、次の処理をする
    if age.isdigit():
        if int(age) >= 0:
            break
    print("0以上の数値を入力してください")
print("入力を受け付けました" + age)
# isdigitはstrで利用できるメソッドです
# 文字列.isdigitで文字列が全て数字の場合はTrue、それ以外はFalseをかえす



