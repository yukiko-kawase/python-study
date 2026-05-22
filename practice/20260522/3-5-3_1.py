import openpyxl

wb = openpyxl.load_workbook("名簿.xlsx")
ws = wb.active
with open("名簿.txt", "w", encoding="utf8") as file:
    for row in ws.values:
        for value in row:
            file.write(value)
        file.write("\n")
