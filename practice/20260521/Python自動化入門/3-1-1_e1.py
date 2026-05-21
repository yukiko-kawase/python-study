import openpyxl

wb = openpyxl.load_workbook("成績.xlsx")
ws = wb.active
# 値が入力されていないセルを指定している
print(ws.cell(row=2, column=3).value)