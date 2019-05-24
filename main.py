from scene import Scene
from sphere import Sphere
from vector import Vector
from material import Material
from ray import Ray
from camera import Camera
from light import Light
from plane import Plane

if __name__=="__main__":

	c_pos = {'x':0.0, 'y':0.0, 'z':0.0}
	c_target = {'x':0.0,'y':0.0,'z':0.0}
	f = {'x':0.0, 'y':0.0, 'z':0.0}
	fov = {'x':0.0, 'y':0.0, 'z':0.0}
	up = {'x':0.0, 'y':0.0, 'z':0.0}
	height = 0.0
	width = 0.0

	def getTxt():
		data = open("input/entrada.txt","r")
		inputs = data.readlines()

		global c_pos,c_target,f,fov,up,height,width

		height = inputs[3].split(' ')[0]
		width = inputs[3].split(' ')[1]

		C_pos_in = inputs[0].replace('\n','').replace('\r','')
		C_target_in = inputs[1].replace('\n','').replace('\r','')
		C_f_in = inputs[2].replace('\n','').replace('\r','')
		C_fov_in = inputs[3].replace('\n','').replace('\r','')
		C_up_in = inputs[4].replace('\n','').replace('\r','')
		C_height_in = inputs[5].replace('\n','').replace('\r','')
		C_width_in = inputs[6].replace('\n','').replace('\r','')

		c_pos['x'] = C_pos_in.split(' ')[0]
		c_pos['y'] = C_pos_in.split(' ')[1]
		c_pos['z'] = C_pos_in.split(' ')[2]

		c_target['x'] = C_target_in.split(' ')[0]
		c_target['y'] = C_target_in.split(' ')[0]
		c_target['z'] = C_target_in.split(' ')[0]

		f['x'] = C_f_in.split(' ')[0]
		f['y'] = C_f_in.split(' ')[1]
		f['z'] = C_f_in.split(' ')[2]

		fov['x'] = C_fov_in.split(' ')[0]
		fov['y'] = C_fov_in.split(' ')[1]
		fov['z'] = C_fov_in.split(' ')[2]

		up['x'] = C_up_in.split(' ')[0]
		up['y'] = C_up_in.split(' ')[1]
		up['z'] = C_up_in.split(' ')[2]
		


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