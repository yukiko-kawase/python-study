# updateメソッドを使うと、別の辞書を使って値を更新できる
# キーがすでに存在する場合は対応する値を上書きし、存在しない場合は、あらたに要素を追加する
profile = {"name":"富士通太郎","age":20}
new_profile ={"age":21,"area":"神奈川県"}
profile.update(new_profile)
print(profile)
