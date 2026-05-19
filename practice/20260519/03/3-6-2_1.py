# 例外処理の実装
# try節の処理を実行する
try:
    # 数値「10」を数値「0」で割った結果を変数numに代入する
    num = 10 / 0
# ZeroDivisionErrorが発生した場合、例外の内容を変数eに代入し、except節の処理を実行する
except ZeroDivisionError as e:
    # 変数eの内容を表示する
    print(e)
# 例外の発生有無にかかわらず、finally節の処理を実行する
finally:
    # 「事後処理」と表示する
    print("事後処理")