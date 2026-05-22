import csv

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
with open("students.csv", "r" ,encoding="utf8") as file:
    for row in csv.reader(file):
        # appendメソッドを使うと読み込んだcsvファイルの１行ずつを、上から下への順に追加される
        ws.append(row)
wb.save("CSVファイル読み込み.xlsx")

"""
append リスト[] 順番あり、重複OK！
add    集合{}   重複なし
"""

