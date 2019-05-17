import math
from Ray import Ray

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
        self.f = f
        self.fov = fov
        self.up = up
        self.viewheigth = float(viewheigth)
        self.viewWidth = float(viewWidth)

        self.alfa = (fov / 180 * PI)/2
        self.f = (self.target - self.e).normalized() #O vetor vai para o centro
        self.s = (self.f.cross(self.up)).normalized() #Eixo X do vetor
        self.u = self.s.cross(self.f) # Eixo Y do vetor

    def CalcRay(self, x, y):
        #Calcula o raio dependendo dos paramentros da camera. x e y. pixels
        pixeWidth = self.width/(self.viewWidth - 1)
        pixeHeigth = self.heigth/(self.viewheigth - 1)
        xcomp = self.s.scale(x*pixeHeigth - self.width/2)
        ycomp = self.u.scale(y*pixeHeigth - self.heigth/2)

        return Ray(self.e, self.f + xcomp + ycomp)       