# 行や列の非表示
import openpyxl

wb = openpyxl.load_workbook("名簿.xlsx")
ws = wb.active
ws.row_dimensions[2].hidden = True
ws.column_dimensions["B"].hidden = True
wb.save("名簿(非表示後).xlsx")