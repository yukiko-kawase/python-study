import openpyxl

wb = openpyxl.load_workbook("資料.xlsx")
ws = wb.active
# valuesを指定するとセルの値を行ごとに読み込むことが可能。
for row in ws.values:
    for value in row:
        print(value)