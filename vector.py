import math

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        #Retorna o vetor unitário
        k = 1/math.sqrt(self.x * self.x + self.y * self.y + self.z + self.z)
        return Vector(self.x*k, self.y*k, self.z*k)
    
    def grandeza(self):
        #Retorna a grandeza do vertor
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def inverte(self):
        #Inverte todos os componentes
        return Vector(-self.x, -self.y, -self.z)

    def __neg__(self):
        #Operador -
        #Inverte todos os componentes
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        #Operador +
        #se passado com Vector, é adicionado os dois vetores
        #Se for passado como escalar, é adicionado o escalar a todos os componentes do vetor

        if type(other).__name__ == 'Vector':
            return self.x + other, self.y + other, self.z + other
        else:
            return Vector(self.x + other, self.y + other, self.z + other)
        
    def __sub__(self, other):
        #Operador -
        #se passado com Vector, é subtraido os dois vetores
        #Se for passado como escalar, é subtraido o escalar a todos os componentes do vetor

        if type(other).__name__ == 'Vector':
            return self.x - other, self.y - other, self.z - other
        else:
            return Vector(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        #Operador *
        #se passado com Vector, é executado o produto de pontos dos dois
        #Se for passado como escalar, é multiplicado o escalar a todos os componentes do vetor

        if type(other).__name__ == 'Vector':
            return self.x * other, self.y * other, self.z * other
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def __mod__(self, other):
        #Operador %
        #Executa o produto cruzado

        return Vector(other.y*self.z-other.z*self.y, -(other.x*self.z-other.z-self.x), other.x*self.y-other.y-self.x)
