from math import sqrt
from math import fabs
class Vector:
    def __init__(self, x=0, y=0, z=0):
        (self.x, self.y, self.z) = (x, y, z)
  

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
    	return self.__mul__(other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)
    def __truediv__(self, other):
    		return Vector(self.x / other, self.y / other, self.z / other)

    def __str__(self):
    		return "Vector({}, {}, {})".format(*self)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    def __pow__(self, exp):
        if exp != 2:
            raise ValueError("Exponent can only be two")
        else:
            return self * self

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def norm(self):
        mag = self.magnitude()
        return Vector(self.x/mag, self.y/mag, self.z/mag)

    def components(self):
        return (self.x, self.y, self.z)
    def invert(self):
        return Vector(-self.x, -self.y, -self.z)

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

   
    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def scale(self, factor):
            return self * factor

    def reflect(self, other):
        other = other.norm()
        return (self - 2 * (self * other) * other)
    def clamp(self,lo,hi,v):
       return max(lo,min(hi,v))

    def refract(self,other, ior):
            #self = direção do ray de indiencia
            cosi = self.clamp(-1,1, self * other)
            etai = 1 #Indice de Refração do meio. Deixamos como padrão 1 (AR)
            etat = ior
            n = other #Normal
            if (cosi < 0 ): 
                cosi = -cosi
            else:
                etai,ior = ior,etai
                n = n.invert()
            eta = float(etai/ior)
            k = float(1 - eta**2 * (1-cosi**2))
            if k < 0: 
                return 0
            else: 
                return eta * self + (eta * cosi - sqrt(k)) * n
                
    def fresnel(self,normal,ior):
        cosi = self.clamp(-1,1, self * normal)
        etai = 1
        etat = ior
        if (cosi < 0 ): cosi = -cosi
        else:
            etai,etat = etat,etai
            normal = normal.invert()
        sint = etai/etat * sqrt(max(0,-1 - cosi * cosi))
        if sint >=1: 
            kr = 1
            return kr
        else:
            cost = sqrt(max(0,1-sint * sint))
            cosi = fabs(cosi)
            rs = ((etat * cosi) - (etai * cost))/ ((etat * cosi) + (etai * cost))
            rp = ((etai * cosi) - (etat * cost))/ ((etai * cosi) + (etat * cost))
            kr = (rs * rs + rp * rp)/2
            return kr
    def pow(self,other):
        return Vector(pow(self.x,other),pow(self.y,other),pow(self.z,other))
    def multi(self,other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

if __name__=="__main__":
    vec1 = Vector(0.25,0.25,0.25)
    vec2 = Vector(0.25,0.5,0.25)
    #DOT
    result_test = vec1 * vec2
    print(result_test)
    #CROSS
    print(vec1.cross(vec2))
    #NORM - UNIT VECTOR
    print(vec1.norm())
    

