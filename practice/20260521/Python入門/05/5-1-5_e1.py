# Accessというクラスを定義（設計図）
class Access:

    # コンストラクタ（インスタンス生成時に自動で呼ばれる）
    def __init__(self, title):
        # __title は「プライベート風」の変数
        # 実際には Python が内部で
        # self._Access__title という名前に変換する（名前マングリング）
        self.__title = title

    # タイトルを表示するメソッド
    def disp_title(self):
        # クラス内部では __title と書ける（自動変換される）
        print(self.__title)


# Accessクラスからインスタンス（実体）を生成
a = Access("アクセス制御")

# ↓これはエラーになる
# 理由：
# __title はそのままの名前では保存されていないため
# 実際の名前は _Access__title になっている
# print(a.__title)


# これはOK
# 理由：
# Pythonが内部で使っている「本当の名前」を直接指定している
print(a._Access__title)


# 内部の状態イメージ
# a
# └── _Access__title = "アクセス制御"
#
# ※ __title という名前の変数が別にあるわけではない（重複なし）


# 正しい使い方（推奨）
# クラス外からはメソッド経由でアクセスする
a.disp_title()


# まとめ
# ・__title は「外から触るな」という目印
# ・実際には _Access__title に変換される
# ・データは1つだけで重複しない
# ・直接アクセスは可能だが非推奨（カプセル化を壊すため）
