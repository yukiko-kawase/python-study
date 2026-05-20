class BodyInfo:
    ideal_bmi = 22

    @classmethod
    def judge_bmi(cls,bmi):
        if bmi > cls.ideal_bmi:
            print("BMIが理想を上回っています")
        elif bmi < cls.ideal_bmi:
            print("理想を下回っています")
        else:
            print("理想のBMIです")

print("理想のBMI：",BodyInfo.ideal_bmi)
BodyInfo.judge_bmi(18)
