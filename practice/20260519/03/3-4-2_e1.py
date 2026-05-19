# よく起きるエラー
# if文の条件の後に「:」をつけ忘れるとエラーになる
age = 10
if age <= 3
    print("幼児")
elif age <= 12:
    print("子供")
else:
    print("大人")