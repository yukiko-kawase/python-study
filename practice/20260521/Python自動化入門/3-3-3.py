"""
シートのコピー
Workbookオブジェクトのcopy_worksheetメソッドを使用し、引数でシートの
変数名(Worksheetクラスのオブジェクト変数)を指定する
なお、コピーするシートは、ブックの最後に追加される(コピー位置は指定できません)
"""
import openpyxl

wb = openpyxl.load_workbook("売上.xlsx")
ws = wb["売上_3月"]
wb.copy_worksheet(ws)
wb.save("売上(コピー後).xlsx")