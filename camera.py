import math
from vector import *

__all__ = ["camera",]

class Camera(object):
    def __init__(self, pos, target, f, fov, up):
        self.pos = pos
        self.target = target
        self.f = f
        self.fov = fov
        self.up = up
        self.view_heigth = 2 * f * math.tan(fov/2.0)
        self.view_width = self.view_heigth * up

        look_at = target - pos
        look_at.normalize()
