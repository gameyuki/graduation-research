class memory:
    #出来事をリストで保存（）
    #保存内容
    #   1.出来事のID
    #   2.出来事の内容
    #   3.出来事の発生時間
    #   4.出来事の発生場所"
    #   5.出来事の重要度
    event =[]
    
    def ev_add(kind,contxt,time,where,important):
        event = [kind,contxt,time,where,important]
    