# 複雑な辞書からの値の取得
value = {"station": [{"name":"品川","prefecture":"東京都","Line":"JR山手線","x":139.738999,"y":35.62876,"postal":1080075,"prev":"","next":"大崎"},
                     {"name":"大崎","prefecture":"東京都","Line":"JR山手線","x":139.738999,"y":35.62876,"postal":1080075,"prev":"品川","next":"五反田"}]}
print(value["station"][0]["name"])