import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
for row in range(1,10):
    for colum in range(1,10):
        ws.cell(row=row, column=colum, value=row*colum)
wb.save("九九.xlsx")

