from camera import *
from vector import*
from light import *

class Scene:
    def __init__(self,camera,objects,lights,width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height

    #TODO METODOS DE RENDERIZAÇÂO E TRACING
    
    def render(self):
        pixels = [[Vector for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.width):
            for x in range(self.height):
                ray = self.camera.calcRay(x,y)
                pixels[x][y] = self.trace_ray(ray)
        return pixels
    
    def trace_ray(self,ray,depth=0, max_depth=5):
        color = Vector(0,0,0)
        

        if depth >= max_depth:
            return color

        intersection = self.get_intersection(ray)
        if intersection is None:
            return color

        obj, dist = intersection
        intersection_pt = ray.point_at_dist(dist)
        surface_norm = obj.surface_norm(intersection_pt)

        for light in self.lights:
            # ambient light
            color = ((obj.material.color * light.color) * (obj.material.ambient * obj.material.lambert))
            # lambert shading - Diffuse
            pt_to_light_vec = (light.pos - intersection_pt).norm()
            pt_to_light_ray = Ray(intersection_pt, pt_to_light_vec)
            if self.get_intersection(pt_to_light_ray) is None:
                lambert_intensity = surface_norm * pt_to_light_vec
                if lambert_intensity > 0:
                    color += obj.material.color * obj.material.lambert * \
                        lambert_intensity * light.color
        
            #specular (reflective) light
            r = ((surface_norm - pt_to_light_vec) * ((pt_to_light_vec * surface_norm)*2))
            n = 2 #Grau de concentração do destaque especular  N > ponto menor
            color += obj.material.specular * light.color * ((r * ray.invert)**n)
        return color
     

    def get_intersection(self, ray):
        
        intersection = None
        for obj in self.objects:
            dist = obj.intersects(ray)
            if dist is not None and (intersection is None or dist < intersection[1]):
                intersection = obj, dist

        return intersection

    def pixels_to_ppm(self,pixels):
        header = "P3 {} {} 255\n".format(len(pixels[0]), len(pixels))
        img_data_rows = []
        for row in pixels:
            pixel_strs = [
                " ".join([str(int(color)) for color in pixel]) for pixel in row]
            img_data_rows.append(" ".join(pixel_strs))
        return header + "\n".join(img_data_rows)








    


                    
