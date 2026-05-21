# 値の取得
import openpyxl

wb = openpyxl.load_workbook("成績.xlsx")
ws = wb.active
print(ws.cell(row=3, column=2).value)
