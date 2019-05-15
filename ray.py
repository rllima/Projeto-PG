
class Ray:
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction.normalize()

	def point_at_dist(self, dist):
		return self.origin + self.direction * dist