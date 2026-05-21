import sys

import openpyxl

bookname = sys.argv[1]
# argvに格納される値はすべて文字列
row_num = int(sys.argv[2])
col_num = int(sys.argv[3])
wb = openpyxl.load_workbook(bookname)
ws = wb.active
print(ws.cell(row=row_num,column=col_num).value)