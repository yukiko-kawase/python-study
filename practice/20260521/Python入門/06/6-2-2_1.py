import openpyxl

wb = openpyxl.load_workbook("資料.xlsx")
ws = wb.active
print(ws.cell(row=2, column=1).value)
