class Material:
    
 def __init__(self, color, specular=0.5, lambert=1, ambient=0.2):
    self.color = color
    self.specular = specular
    self.lambert = lambert
    self.ambient = ambient