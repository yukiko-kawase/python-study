# よく起きるエラー
# ブロック内でインデントを合わせないとエラーになる
age = 10
if age <= 3:
    print("幼児")
    print("入場料 : 無料")
elif age <= 12:
    print("子供")
        print("入場料 : 300円")
else:
    print("大人")
    print("入場料 : 500円")