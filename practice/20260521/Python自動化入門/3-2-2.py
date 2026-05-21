# 行や列の削除
import openpyxl

wb = openpyxl.load_workbook("名簿.xlsx")
ws = wb.active
ws.delete_rows(1, amount=2)
ws.delete_cols(2)
wb.save("名簿(削除後).xlsx")