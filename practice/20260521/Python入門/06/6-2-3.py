import openpyxl
# Excelのブックを新規作成
wb = openpyxl.Workbook()
ws = wb.active
# cellメソッドを使用して1行1列目に値を入力する
ws.cell(row=1, column=1, value="富士通 太郎")
wb.save("新規資料.xlsx")
