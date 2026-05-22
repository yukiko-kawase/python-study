# シートの削除
import openpyxl

wb = openpyxl.load_workbook("売上.xlsx")
ws = wb["売上_3月"]
wb.remove(ws)
wb.save("売上(削除後).xlsx")