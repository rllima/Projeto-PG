import math
from vector import*
from ray import*

class Camera:
    def __init__(self, pos, target, f, fov, up,yResolution,xResolution):
        self.pos = pos
        self.target = target
        self.f = f
        self.fov = fov
        self.up = up
        self.viewPlaneHalfWidth = math.tan(fov/2.0)
        aspectRatio = yResolution/xResolution
        self.viewPlaneHalfHeight  = aspectRatio*self.viewPlaneHalfWidth

        look_at = target - pos
        self.look_at = look_at.norm()

        self.view_x_axis = Vector.cross(up, look_at) # Vector U 
        self.view_y_axis = Vector.cross(look_at, self.view_x_axis) #Vector V

        self.viewPlaneBottomLeftPoint = self.target- self.view_y_axis*self.viewPlaneHalfHeight - self.view_x_axis*self.viewPlaneHalfWidth
        self.xIncVector = (self.view_x_axis*2* self.viewPlaneHalfWidth)/xResolution;
        self.yIncVector = (self.view_y_axis*2*self.viewPlaneHalfHeight)/yResolution;
    
    def makeRay(self, x,y):
        viewPlanePoint = self.viewPlaneBottomLeftPoint + (self.xIncVector*x) + (self.yIncVector*x)
        castRay = Vector(0,0,0) - self.pos
        return Ray(self.pos,castRay)
        


