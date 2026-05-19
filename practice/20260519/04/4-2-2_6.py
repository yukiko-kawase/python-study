import tkinter

root = tkinter.Tk()
root.title("hello window")
root.minsize(320,240)
hello_Label = tkinter.Label(root,text="こんにちは",font=("メイリオ", 12,"bold"))
hello_Label.pack()
input_Label = tkinter.Label(root,text="名前を入力してください",font=("メイリオ",12,"bold"))
input_Label.pack()
name_entry = tkinter.Entry(root)
name_entry.pack()
name_buttun = tkinter.Button(root,text="名前を入力")
name_buttun.pack()



def hello_name():
    input_name = name_entry.get()
    display_text = "こんにちは、" + input_name +"さん"
    hello_Label["text"] = display_text


name_buttun["command"] = hello_name
root.mainloop()