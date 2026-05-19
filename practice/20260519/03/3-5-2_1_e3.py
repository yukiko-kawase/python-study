# 関数定義よりも先に関数を呼び出そうとするとエラーになる
result = add(10,20)
print(result)

def add(x,y):
    total = x + y
    return total