import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
with open("member.txt", "r", encoding="utf8") as file:
    row_num = 1
    for name in file:
        # テキストファイルを１行ずつ代入すると、末尾に改行コードが含まれた状態になる
        # 文字列型のデータが持つメソッドであるstripメソッドを使うと、文字列の末尾にある
        # 改行コードのような見えない文字を削除できる
        ws.cell(row=row_num, column=1, value=name.strip())
        row_num += 1
        
wb.save("テキストファイル読み込み.xlsx")