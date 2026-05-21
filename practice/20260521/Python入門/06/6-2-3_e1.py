import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.cell(row=1, column=1, value="富士通太郎")
# 保存先フォルダがないとエラーになる
wb.save()
