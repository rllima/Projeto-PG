
class Ray(object):
	#Esta classe representa um raio com uma origem e uma direção
	def __init__(self, origin, direction):
		self.origin = origin #ponto
		self.direction = direction.normalized() #vetor
	
	def pointParametro(self, t):
		#Retorna um ponto neste raio em um determinado parametro t
		return self.origin + self.direction.scale(t)

	def __rep__(self):
		#retorna uma representação de si mesmo
		return 'Ray(%s, %s)' %(repr(self.origin), repr(self.direction))

	def point_at_dist(self, dist):
		return self.origin + self.direction * dist
	
	def invert(self):
		return Ray(self.origin, self.direction.invert())