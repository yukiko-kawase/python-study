import openpyxl
wb = openpyxl.load_workbook("資料.xlsx")
ws = wb.active
# 値が入力されていないセルを指定している場合は、Noneが表示される
print(ws.cell(row=1, column=3).value)