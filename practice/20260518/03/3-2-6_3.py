# 「辞書名.setdefault("キー",値)のように実行することで、指定したキーが辞書に存在しない場合に
# 要素（キーと値）を追加し、その追加した要素の値を戻り値として返す。
# キーが存在する場合は、そのキーを返す
profile = {"name":"富士通太郎","age":20}
profile.setdefault("area","東京都")
print(profile)