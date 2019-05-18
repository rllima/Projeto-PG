#!/usr/bin/env python3.2

from math import *
from ray import *
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

    def __init__(self, pos, target, dist, fov, up, viewheigth, viewWidth):
        self.pos = pos
        self.target = target
        self.dist = 90
        self.fov = fov
        self.up = up
        self.viewheigth = float(viewheigth)
        self.viewWidth = float(viewWidth)

        self.alpha = (fov / 180 * pi)/2
        self.height = 2 * tan(self.alpha)
        self.width = (self.viewWidth/self.viewheigth) * self.height
        self.f = (self.target - self.pos).norm() #O vetor vai para o centro
        self.s = (self.f.cross(self.up)).norm() #Eixo X do vetor
        self.u = self.s.cross(self.f) # Eixo Y do vetor

    def CalcRay(self, x, y):
        #Calcula o raio dependendo dos paramentros da camera. x e y. pixels
        pixeWidth = self.width/(self.viewWidth - 1)
        pixeHeigth = self.height/(self.viewheigth - 1)
        xcomp = self.s.scale(x*pixeHeigth - self.width/2)
        ycomp = self.u.scale(y*pixeHeigth - self.height/2)

        return Ray(self.pos, self.f + xcomp + ycomp) 

    def dist(self, dist):
        self.d = self.size.x / (2*math.tan((dist / 2.0) / 180.0 * math.pi))
        return self.d


if __name__=="__main__":
    c = Camera(Vector(0.0, 0.0, 0.0), Vector(0.0, 0.0, 100.0), 1.0, 90.0, Vector(0, 1, 0), 680, 440)
    for x in range(5):
        for y in range(5):
            print(c.CalcRay(x, y))
   