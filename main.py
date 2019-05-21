from scene import Scene
from sphere import Sphere
from vector import Vector
from material import Material
from ray import Ray
from camera import Camera
from light import Light

if __name__=="__main__":
	Point = Vector
	Color = Vector
	objects = [
		Sphere(
			Point(10, 30, -10), 4, Material(Color(0, 0, 0xFF),
			specular=0.3,material_type="REFLECT_AND_REFRACTION", kt=0.5, kr=1.5)),
			Sphere(
			Point(20, 30, -50), 20, Material(Color( 0xFF, 0, 0xFF),
			specular=0.0, ambient=0.5, lambert=0.8))
		]
	lights = [Light(Point(10, 30, -1), Color(0.1,0.3,0.1))]
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