"""
概要
税込価格を計算する関数を定義
処理の流れ
引数として価格(price)を受け取るto_tax_inclusive_price関数を定義する
price関数内で引数priceに1.1かけ、結果を戻り値として呼び出しもとに返す
備考
少数点から整数の返還には、int関数を使用する
"""
def to_tax_inclusive_price(price):
    tax_calculation = price * 1.1
    return int(tax_calculation)

price = int(input("税抜価格を入力=>"))
price_with_tax = to_tax_inclusive_price(price)
print("税込価格：" + str(price_with_tax))