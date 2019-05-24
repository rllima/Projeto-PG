from math import *
from ray import Ray
from vector import *

class Camera(object):
    #Essa classe descreve a camera
    #fov = fieldOfView (angulo entre o tamanho da porta de visualização e a distancia até a camera)
    #pos = posição do "olho" no espaço (posicao da camera) - ponto
    #target = Ponto de mira (ponto da camera) - ponto
    #up - direção perpendicular a direção em q o "olho" ta apontando - vetor
    #dist = distancia do "olho" até o plano
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
        self.f = (self.target - self.pos).norm() #O vetor vai para o centro/ vetor de direção da camera normalizado 
        self.s = self.f.cross(self.up).norm() #Eixo X do vetor positivo do espaço da camera
        self.u = self.s.cross(self.f) # Eixo Y do vetor 
        self.alpha = ((self.fov/180) * pi)/2
        self.height = 2 * tan(self.alpha) #angulo de abertura da camera
        self.width = (self.view_width/self.view_height) * self.height

        


