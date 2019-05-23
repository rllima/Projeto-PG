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
    
    def trace_ray(self,ray,depth=0, max_depth=15):
        
        color = Vector(0,0,0) # Cor do raio
        
        
        if depth >= max_depth:
            return color

        intersection = self.get_intersection(ray)
        if intersection is None:
            return color

        obj, dist = intersection
        intersection_pt = ray.point_at_dist(dist) #ponto de intersecção
        surface_norm = obj.surface_norm(intersection_pt) #normal a direção do ponto
        bias = 0.000001
        #CALC EFECTS LIGHT

        
        if(obj.material.material_type == "REFLECT_AND_REFRACTION"):
            kr = ray.direction.fresnel(surface_norm,obj.material.kt,obj.material.kr)
            #kr = obj.material.kr
            reflect_dir = ray.direction.reflect(surface_norm).norm()
            reflected_ray_origin = intersection_pt * reflect_dir
            refraction_dir = ray.direction.refract(surface_norm,obj.material.kr).norm()
            refraction_ray_origin = intersection_pt * refraction_dir

            if reflected_ray_origin < 0:
                refle_origin = intersection_pt - surface_norm * bias
            else:
                refle_origin = intersection_pt + surface_norm * bias

            if refraction_ray_origin < 0:
                refra_origin = intersection_pt - surface_norm * bias
            else:
                refra_origin = intersection_pt + surface_norm * bias

            reflected_ray = Ray(refle_origin, reflect_dir)
            refraction_ray = Ray(refra_origin, refraction_dir)
            color += self.trace_ray(reflected_ray, depth + 1) * kr #Traçando raios de reflexão
            color+=self.trace_ray(refraction_ray,depth + 1) * (1- kr)
            color+= obj.material.color * obj.material.kt
            return color
        elif obj.material.material_type =="REFLECT":
            reflect_dir = ray.direction.reflect(surface_norm).norm()
            reflected_ray_origin = intersection_pt * reflect_dir
            if reflected_ray_origin < 0:
                refle_origin = intersection_pt - surface_norm * bias
            else:
                refle_origin = intersection_pt + surface_norm * bias
            
            reflected_ray = Ray(refle_origin, reflect_dir)
            color += self.trace_ray(reflected_ray, depth + 1)  #Traçando raios de reflexão

        for light in self.lights:
            # ambient light
            ambient = (obj.material.color * obj.material.ambient)
            color += ambient
            # lambert shading - Diffuse
            pt_to_light_vec = (light.pos - intersection_pt).norm()
            pt_to_light_ray = Ray(intersection_pt, pt_to_light_vec)
            if self.get_intersection(pt_to_light_ray) is None:
                lambert_intensity = surface_norm * pt_to_light_vec
                if lambert_intensity > 0:
                    lambert = (obj.material.color * ((obj.material.lambert * lambert_intensity)))
                    color += lambert
        
           
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
    

    
            


 








    


                    
