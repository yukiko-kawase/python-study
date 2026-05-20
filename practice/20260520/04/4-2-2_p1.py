"""
概要
年明けまでのカウントダウンを1秒ごとに表示する
処理の流れ
日付を扱うために必要なdatetimeモジュール、算術計算のためのmathモジュールを読み込む
今日の西暦を取得
来年の1月1日の時刻を生成する
無限ループで1秒ごとに来年の1月1日までの時間「〇日〇時間〇分〇秒」の形式で表示する
無限ループにおける処理の詳細
1秒休む
現在の日時を取得する
来年の1月1日から差を取得する
取得した差を〇日〇時間〇分〇秒の形式で表す
差を表示する
"""
import datetime
import time
import math

year = datetime.datetime.now().year
new_year_day = datetime.datetime(year + 1,1,1)
while True:
    time.sleep(1)
    now = datetime.datetime.now()

    diff = new_year_day-now
    diff_hours = math.floor(diff.seconds/3600)
    diff_minutes = math.floor(diff.seconds % 3600 /60)
    diff_seconds = diff.seconds % 3600 % 60

    print("年明けまで あと",
          diff.days,("日"),
          diff_hours,"時間",
          diff_minutes,"分",
          diff_seconds,"秒")


