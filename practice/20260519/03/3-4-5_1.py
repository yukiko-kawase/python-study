for i in range(10):
    if i == 4:
        # continueで繰り返し処理の先頭へ遷移する
        continue
    elif i == 8:
        # breakで繰り返し処理から抜ける
        break
    print(i)