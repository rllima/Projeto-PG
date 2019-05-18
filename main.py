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
			Point(150, 120, -20), 80, Material(Color(0xFF, 0, 0),
			specular=0.2)),
		Sphere(
			Point(420, 120, 0), 100, Material(Color(0, 0, 0xFF),
			specular=0.8)),
		Sphere(Point(320, 240, -40), 50, Material(Color(0, 0xFF, 0))),
		Sphere(
			Point(300, 200, 200), 100, Material(Color(0xFF, 0xFF, 0),
			specular=0.8)),
		Sphere(Point(300, 130, 100), 40, Material(Color(0xFF, 0, 0xFF))),
		Sphere(Point(300, 1000, 0), 700, Material(Color(0xFF, 0xFF, 0xFF),
			lambert=0.5)),
		]
	lights = [Light(Point(200, -100, 0), Color(0.1,0.3,0.1))]
	c_pos = Vector(300, 200, 200)
	c_target = Vector(420, 120, 0)
	f=1
	fov=45
	up=Vector(1,0,0)
	camera = Camera(c_pos,c_target,f,fov,up,640,480)
	scene = Scene(camera, objects, lights, 640,480)
	pixels = scene.render()
	with open("image.ppm", "w") as img_file:
		img_file.write(scene.pixels_to_ppm(pixels))