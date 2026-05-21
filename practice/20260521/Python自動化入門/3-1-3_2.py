import openpyxl
file_path = ("部署人数.xlsx")
wb = openpyxl.load_workbook(file_path,data_only=True)
ws = wb.active
print(ws.cell(row=5, column=2).value)

