# 行ごとに値を読み込む
import openpyxl

wb = openpyxl.load_workbook("成績.xlsx")
ws = wb.active
for row in ws.values:
    breakpoint()
    for value in row:
        breakpoint()
        print(value)