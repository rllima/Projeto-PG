from math import sqrt
class Vector:
    def __init__(self, x=0, y=0, z=0):
        (self.x, self.y, self.z) = (x, y, z)
  

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

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