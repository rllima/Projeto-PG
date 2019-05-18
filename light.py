from vector import*
class Light:
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color

    def getSouce(self):
        return self.pos

