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
			Point(-8.1, 0, 8.1), 8, Material(Color(0xFF, 0, 0),
			specular=0.2)),
			Sphere(
			Point(8.1, 0, 8.1), 8, Material(Color(0xFF, 0xFF, 0),
			specular=0.2)),
			Sphere(
			Point(8.1, 15, 10), 8, Material(Color(0, 0xFF, 0),
			specular=0.2))
		]
	lights = [Light(Point(0, 30, 0), Color(255,255,255))]
	c_pos = Vector(0,60,-110)
	c_target = Vector(0,0,0)
	f=10
	fov=40
	up=Vector(0,1,0)
	camera = Camera(c_pos,c_target,f,fov,up,640,480)
	scene = Scene(camera, objects, lights, 640,480)
	pixels = scene.render()
	with open("image.ppm", "w") as img_file:
		img_file.write(scene.pixels_to_ppm(pixels))