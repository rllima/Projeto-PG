import numpy as np
class Vector:
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def norm(self):
        mag = np.sqrt(abs(self))
        return self * (1.0 / np.where(mag == 0, 1, mag))
    def components(self):
        return (self.x, self.y, self.z)
    def invert(self):
        return Vector(-self.x, -self.y, -self.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    @staticmethod
    def cross(v0, v1):
        return Vector(v0.y * v1.z - v0.z * v1.y,
                      v0.z * v1.x - v0.x * v1.z,
                      v0.x * v1.y - v0.y * v1.x)