"""
Tkinterモジュールをインポートしたあと、tkinter.Tk()でウィンドウを作成し、mainioopメソッドでウィンドウを表示
ウィンドウの上部タイトルやウィンドウサイズを設定することも可能
ウィンドウに文字列を表示する際はtkinter.Labelを使ってラベルを作成する
この時、引数でフォントの設定などもできる
"""
import tkinter

root = tkinter.Tk()
root.title("hello window")
root.minsize(320,240)
hello_label = tkinter.Label(root,text="こんにちは", font=("メイリオ",12,"bold"))
hello_label.pack()
root.mainloop()