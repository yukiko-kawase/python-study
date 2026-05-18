number_List =[10,20,30]
# リストの範囲を超えたインデックスを指定すると、エラーになる
print(number_List[3])
print(number_List[1:3])
number_List[1] = 21
print(len(number_List))
number_List.append(40)
print(number_List[3])
print(number_List)
