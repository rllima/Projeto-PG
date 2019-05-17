class Color(object):
    #Vai descrver as cores dos objetos

    def __init__(self, r, g, b):
        #O construtor verifica se os componentes dados então entre 0 e 255
        self.r = max(min(r, 255), 0)
        self.g = max(min(g, 255), 0)
        self.b = max(min(b, 255), 0)
    
    def __add__(self, c):
        #Adiciona duas cores
        return Color(min(self.r + c.r, 255), min(self.g + c.g, 255), min(self.b + c.b, 255))
    
    def __mult__(self, f):
        #Multiplica cada componente de cor com um determinado fator

        r = max(min(self.r * f, 255), 0)
        g = max(min(self.g * f, 255), 0)
        b = max(min(self.b * f, 255), 0)
        return Color(r, g, b)