# 「r」モードを指定してopen関数を呼び出した場合、戻り値に対してwriteメソッドを呼び出すとエラーになる
with open("subject.txt", "r", encoding="utf8") as file:
    file.write("国語\n数学\n理科\n社会")