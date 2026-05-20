class BodyInfo:
    # クラス変数の定義
    ideal_bmi = 22
    # コンストラクタの定義
    def __init__(self, height,weight):

        # インスタンス変数の定義
        self.height = height
        self.weight = weight

    # メソッドの定義
    def calc_weight_for_bmi(self, bmi):
        return self.height ** 2 * bmi

# オブジェクトの生成
body1 = BodyInfo(1.55,48)
body2 = BodyInfo(1.70,68)


print(body1.calc_weight_for_bmi(19))
print(BodyInfo.calc_weight_for_bmi(body2,19))