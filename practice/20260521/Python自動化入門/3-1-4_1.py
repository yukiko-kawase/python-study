# パラメータ
import openpyxl

bookname = input("ブック名を入力してください=>")
row_num = int(input("行番号を入力してください=>"))
col_num = int(input("列番号を入力してください=>"))

wb = openpyxl.load_workbook(bookname)
ws = wb.active
print(ws.cell(row=row_num, column=col_num).value)

