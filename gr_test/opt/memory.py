class memory:
    #出来事をリストで保存（）
    #保存内容
    #   1.出来事のID
    #   2.出来事の内容
    #   3.出来事の発生時間
    #   4.出来事の発生場所"
    #   5.出来事の重要度
    event = []
    
    #イベントの追加
    def ev_add(event,kind,contxt,time,where,important):
        event.append([kind,contxt,time,where,important])
    
    #イベントを返す
    #引数をもう少し考える
    def return_event(event,ID):
        return event[ID]
    
    #イベントの検索
    #　TODO:検索方法を考える
    def Is_check_event(event,ID):
        if event[ID] == None:
            return 0
        else:
            return 1
    