from math import *
from ray import Ray
from vector import *

class Camera(object):
    #Essa classe descreve a camera
    #fov = fieldOfView
    #pos = posição
    #target = Ponto de mira
    #up vetor que aponta direção
    #dist = distancia
    #viewWidth = largura da imagem
    #viewheigth = Altura da imagem

    def __init__(self, pos, target, dist, fov, up, view_height, view_width):
        self.pos = pos
        self.target = target
        self.dist = dist
        self.fov = fov
        self.up = up
        self.view_height = view_height
        self.view_width = view_width
        self.cam_calc()
        

    def calcRay(self, x, y):
        #Calcula o raio dependendo dos paramentros da camera. x e y. pixels
        pixelWidth = self.width / self.view_width
        pixelHeight = self.height / self.view_height
        xcomp = self.s * (x * pixelWidth - self.width / 2)
        ycomp = self.u * (y * pixelHeight - self.height / 2)
        return Ray(self.pos, (self.f + xcomp + ycomp).norm())
  
    def cam_calc(self):
        self.pos = Vector(self.pos.x, self.pos.y,self.pos.z * self.dist)
        self.up = self.up.norm()
        self.f = (self.target - self.pos).norm()
        self.s = self.f.cross(self.up).norm()
        self.u = self.s.cross(self.f)
        self.alpha = ((self.fov/180) * pi)/2
        self.height = 2 * tan(self.alpha)
        self.width = (self.view_width/self.view_height) * self.height

        


