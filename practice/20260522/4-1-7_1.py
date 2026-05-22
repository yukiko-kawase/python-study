# 表記ゆれの統一
import unicodedata

import openpyxl

wb = openpyxl.load_workbook("クラス名簿.xlsx")
ws = wb.active
for row in ws["A1:B4"]:
    for wc in row:
        wc.value = unicodedata.normalize("NFKC",wc.value)
wb.save("クラス名簿(表記統一後).xlsx")