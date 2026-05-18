"""
getメソッド
「辞書名["キー"]」のように値を取得するときと同様に使うことができる
「辞書名.get("キー")」として値を取得する
"""
profile = {"name":"富士通太郎","age":20}
print(profile.get("name"))
print(profile.get("Name"))
