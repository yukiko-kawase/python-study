# よく起きるエラー
try:
    num = 10 / 0
# except節で指定していない例外が発生した場合、エラーとなる
except TypeError as e:
    print(e)
finally:
    print("事後処理")
# この場合の対処は、TypeErrorではなくZeroDivisionError as eを指定する

