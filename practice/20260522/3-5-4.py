# Excelファイルの内容をPDFファイルとして保存したい場合は、外部ライブラリのwin32comライブラリを使用する
import pathlib

import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
input_path = pathlib.Path("売上.xlsx")
output_path = pathlib.Path("売上.pdf")
workbook = excel.Workbooks.Open(str(input_path.resolve()))
workbook.ExportAsFixedFormat(Type=0, Filename=str(output_path.resolve()))
workbook.Close(SaveChanges =False)
excel.Quit()
