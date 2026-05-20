class BodyInfo:
    ideal_bmi = 22

    def __init__(self, height ,weight):
        self.height = height
        self.weight = weight

    def calc_weight_for_bmi(self,bmi):
        return self.height ** 2 * bmi
# 渡す引数がたりない
body1 = BodyInfo(1.55)
body2 = BodyInfo(1,70, 68)
print(body1.calc_weight_for_bmi(19))
print(BodyInfo.calc_weight_for_bmi(body2, 19))
