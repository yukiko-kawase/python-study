# 複数シートの一括設定

import openpyxl

wb = openpyxl.load_workbook("売上.xlsx")
# ブックの変数名.worksheetsですべてのシートを取得する
for ws in wb.worksheets:
    ws.title += "度"
wb.save("売上(一括変更後).xlsx")