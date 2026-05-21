"""
シートを移動するには、Workbookオブジェクトのmove_sheetメソッドを使用し、引数で移動するシート名
またはシートの変数名(Worksheetクラスのオブジェクト変数)を指定し、続けてキーワード引数offsetで移動する数を指定する
キーワード引数offsetに正の数を指定すると後ろに移動し、負の数を指定すると前に移動する
"""
import openpyxl

wb = openpyxl.load_workbook("売上.xlsx")
wb.move_sheet("売上_1月", offset=2)
wb.move_sheet("売上_3月", offset=-1)
wb.save("売上(移動後).xlsx")
