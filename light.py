from Color import *

class Ligth(object):
    #Descreve a posição e uma cor de uma fonte de luz
    def __init__(self, position, color = (255, 255, 255,)):
        self.position = position
        self.color = Color(color[0], color[1], color[2])