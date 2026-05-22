from openpyxl import load_workbook

wb = load_workbook("経費.xlsx")
ws = wb.active
ws.row_dimensions[1].height = 40
ws.column_dimensions["B"].width = 15
wb.save("経費(高さ幅設定後).xlsx")
