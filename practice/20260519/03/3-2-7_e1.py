# 集合はインデックスを持たないため、特定の値を取り出すことはできない
# もし、値を取り出したい場合は、リストやタプルなどを使用する
number_set = {10,20,30}
number_set.add(40)
number_set.add(10)
print(number_set[0])
