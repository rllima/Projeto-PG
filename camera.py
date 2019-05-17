import math
from vector import*

class Camera:
    def __init__(self, pos, target, f, fov, up):
        self.pos = pos
        self.target = target
        self.f = f
        self.fov = fov
        self.up = up
        self.view_heigth = 2 * f * math.tan(fov/2.0)
        self.view_width = up * self.view_heigth

        look_at = target - pos
        look_at.norm()
        self.view_center = pos + look_at * f #f = distancia

        up = Vector(0.0, 1.0, 0.0)
        self.view_x_axis = Vector.cross(up, look_at)
        self.view_y_axis = Vector.cross(look_at, self.view_x_axis)

    
    def getPos(self):
        return self.pos
    
    def getTarget(self):
        return self.target
    
    def getf(self):
        return self.f
    
    def getFov(self):
        return self.fov
    
    def getUp(self):
        self.up
    
    def getWidth(self):
        return self.view_width

    def getHeigth(self):
        return self.view_heigth
    
    def getCenter(self):
        return self.view_center
    
    def getViewXAxis(self):
        return self.view_x_axis
    
    def getViewYAxis(self):
        return self.view_y_axis
    
if __name__=="__main__":
    c = Camera(Vector(0.0, 0.0, 0.0), Vector(0.0, 0.0, 100.0), 1.0, 90.0, Vector(0.0, 1.0, 0.0))
    print(c.getWidth())
    print(c.getHeigth  ())
    print(c.getCenter().x)
    print(c.getCenter().y)
    print(c.getCenter().z)
    print(c.getViewXAxis().x)
    print(c.getViewXAxis().y)
    print(c.getViewXAxis().z)
    print(c.getViewYAxis().x)
    print(c.getViewYAxis().y)
    print(c.getViewYAxis().z)
