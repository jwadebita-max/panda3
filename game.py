from direct.showbase.showbase import ShowBase 

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
base = ShowBase()
base.run()