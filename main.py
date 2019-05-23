from scene import Scene
from sphere import Sphere
from vector import Vector
from material import Material
from ray import Ray
from camera import Camera
from light import Light
from plane import Plane

if __name__=="__main__":
	Point = Vector
	Color = Vector
	objects = [
		Sphere(Point(40, 69, -50), 10, Material(Color(0, 0xFF, 0xFF),specular=0.5,material_type="REFLECT")),
		Sphere(Point(5, 55, -10), 4, Material(Color(0, 0, 0xFF),specular=0.3,material_type="REFLECT")),
		Sphere(Point(20, 60, -30), 20, Material(Color( 0xFF, 0, 0xFF),specular=0.2, ambient=0.5,kr=1.9, lambert=0.8,material_type="REFLECT_AND_REFRACTION")),
		Plane(Point(0, 0, 0), Point(0, 30,10), Material(Color(128, 128, 128),specular=0.3, ambient=0.5, lambert=0.01))
	]

	lights = [Light(Point(20, 100, -30), Color(0.1,0.3,0.1))]
	c_pos = Vector(20, 30, 4)
	c_target = Vector(20, 50, -10)
	f = 20
	fov=45
	up=Vector(1,0,0)
	camera = Camera(c_pos,c_target,f,fov,up,640,480)
	scene = Scene(camera, objects, lights, 640,480)
	pixels = scene.render()
	with open("image.ppm", "w") as img_file:
		img_file.write(scene.pixels_to_ppm(pixels))