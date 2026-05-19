number_list = [10,20,30]
try:
    print(number_list[3])
except IndexError as e:
    print("IndexErrorです")