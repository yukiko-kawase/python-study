import openpyxl

wb = openpyxl.load_workbook("売上.xlsx")
ws_origin = wb["売上_3月"]
ws_copied = wb.copy_worksheet(ws_origin)
ws_copied.title = "売上_3月(コピー)"
wb.save("売上(名前変更後).xlsx")
