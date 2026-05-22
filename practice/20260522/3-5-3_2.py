import csv

import openpyxl

wb = openpyxl.load_workbook("売上.xlsx")
ws = wb.active
with open("売上.csv", "w", encoding="utf8") as file:
    csv_writer = csv.writer(file)
    # ws.valuesでシート全体のデータを取得できる
    # writerrowsメソッドを使うとまとめて書き込むことができる
    csv_writer.writerows(ws.values)