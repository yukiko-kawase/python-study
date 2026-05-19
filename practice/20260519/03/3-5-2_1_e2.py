# 関数に設定された引数を渡さないとエラーになる
def add(x,y):
    total = x + y
    return total
# 関数に渡す引数yに渡す引数がない
result = add(10)
print(result)