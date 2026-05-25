from openpyxl import load_workbook

wb = load_workbook("practice/20260525/販売データ.xlsx")
ws = wb.active
ws.freeze_panes = "A2"
wb.save("practice/20260525/販売データ(行表示固定後).xlsx")