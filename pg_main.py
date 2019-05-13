import math
import numpy as np


class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return np.linalg.norm(self)
    def normalize(self):
        return Vector(self.x /self.norm(),self.y/self.norm(), self.z/self.norm())
    def add(self, other):
        return np.add(self, other)
    def sub(self, other):
        return np.subtract(self,other)
    def mult(self, other):
        return np.dot(self,other)

#Como  requisitado na descrição do projeto, para o algoritmo de Ray Tracing, o objeto a ser utilizado
#deve ser a esfera, definida em termo do raio, e do seu centro
class Sphere:
    def __init__(self,origin,radius):
        self.origin = origin
        self.radius = radius

    #Decidimos tornar o calculo de intersecção dentro do prorio objeto, facilitando a modularidade, pois para cada
    #forma, teremos um modo de calculo diferente de intersectção

    def intersec(self, ray):

        """
            Se o raio(aqui se referindo ao raio camera -> objeto), intersecta a esfera 
            então devemos retornar a distancia entre o ponto de intercção e os olhos, caso
            contrario retornamos None
        """

        ray_to_sphere = ray.origin - self.origin #Representa a distancia entre o inicio do raio e a posição do circulo
        b = 2* np.dot(ray.direction,ray_to_sphere)
        c = ray_to_sphere ** 2 - self.radius ** 2
        discriminant = b ** 2 - 4 * c

        if discriminant >= 0:
            dist = (-b - math.sqrt(discriminant))/2
            if dist > 0:
                return dist 

        