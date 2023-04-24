import memory

class agent(memory):
    def __init__(self):
        self.name = "agent"
        self.memory = memory()

    #計画
    #第一引数　出来事
    #第二引数　記憶　違うかも
    def plan():
        return 0
    
    #記憶の追加
    def mem_add(event,kind,contxt,time,where,important):
        memory.ev_add(event,kind,contxt,time,where,important)
        return 0

    #状況の把握(観察)
    def observe():
        return 
        
    #行動
    # 基本ずっと回す
    def action():
            ob = observe()
            mem_add()
            plan()
    
    
    #変数
    
    #状態変数
    
    