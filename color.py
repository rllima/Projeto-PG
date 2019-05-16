class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __add__(self, other):
        #Operador +
        if type(other).__name__=='Color':
            return Color(self.r+other, self.g+other.g, self.b+other.b)
        else:
            return Color(self.r+other, self.g+other, self.b+other)
    
    def __mult__(self, f):
        #Operador *
        f type(other).__name__ == 'Color':
            return Color(self.r*other.r, self.g*other.g, self.b*other.b)
        else:
            return Color(self.r*other, self.g*other, self.b*other)