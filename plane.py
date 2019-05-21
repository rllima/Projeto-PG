from vector import Vector
import math

class Plane(object):
    def __init__(self, point, normal, material):
        self.point = point
        self.normal = normal
        self.material = material
    
    def __repr__(sel):
        return 'Plane(% s, % s)' % (repr(self.point), repr(self.normal))

    def intersects(self, ray):
        op = ray.origin - self.point
        a = Vector.dot(op, self.normal)
        b = Vector.dot(ray.direction, self.normal)
        if b < 0:
            return -a/b
        else:
            return None

    # def surface_norm(self, point):
    #     return (point - self.origin).norm()

    def surface_norm(self, p):
        return self.normal
    
    def getMaterialReflection(self):
        return self.material.reflects
    
    def getBaseColor(self):
        return self.material.getBaseColor()