# 戻り値が複数の関数
def calc(x,y):
    total = x + y
    difference = x - y
    return total,difference

plus,minus = calc(30,20)
print("plus:" + str(plus))
print("minus" + str(minus))
