import openpyxl

empno = input("従業員番号を入力してください=>")
name = input("氏名を入力してください=>")
dept = input("部署名を入力してください=>")

title_list = ["従業員番号","氏名", "部署名"]
content_list = [empno, name, dept]
input_lists = [title_list,content_list]

wb = openpyxl.Workbook()
ws = wb.active

row = 0
# value["従業員番号","氏名","部署名"]input_lists[["従業員番号","氏名", "部署名"],[empno, name, dept]]
for value_list in input_lists:
    row += 1
    column = 0
    # value[従業員番号]
    for value in value_list:
        column += 1
        ws.cell(row=row, column=column, value =value)




wb.save("従業員情報.xlsx")

