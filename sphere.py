import math
#Como  requisitado na descrição do projeto, para o algoritmo de Ray Tracing, o objeto a ser utilizado
#deve ser a esfera, definida em termo do raio, e do seu centro
class Sphere:
    def __init__(self,origin,radius, material):
        self.origin = origin
        self.radius = radius
        self.material = material

    #Decidimos tornar o calculo de intersecção dentro do prorio objeto, facilitando a modularidade, pois para cada
    #forma, teremos um modo de calculo diferente de intersectção

    def intersects(self, ray):

        """
            Se o raio(aqui se referindo ao raio camera -> objeto), intersecta a esfera 
            então devemos retornar a distancia entre o ponto de intercção e os olhos, caso
            contrario retornamos None
        """

        ray_to_sphere = ray.origin - self.origin #Representa a distancia entre o inicio do raio e a posição do circulo
        b = 2 * (ray.direction * ray_to_sphere)
        c = ray_to_sphere ** 2 - self.radius ** 2
        discriminant = b ** 2 - 4 * c

        if discriminant >= 0:
            dist = (-b - math.sqrt(discriminant))/2
            if dist > 0:
                return dist 

                
    """
        Um normal é, em cada ponto da superfície de uma esfera ou de algum outro objeto, um vetor que é perpendicular
        à superfície e irradia para fora. Precisamos saber isso para que possamos calcular a maneira como um raio
        reflete uma esfera
    """    
    def surface_norm(self, point):
        return (point - self.origin).norm()