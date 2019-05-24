class Material:
    
 def __init__(self, color,specular=0.5, lambert=1, ambient=0.2, material_type="DIFFUSE",kr=1.5,kt=0.5):
    self.color = color
    self.specular = specular #ks
    self.lambert = lambert #kd
    self.ambient = ambient #ka
    self.material_type = material_type #Tipo do Material
    self.kr = kr #Indice de refração do obejto
    self.kt = kt #Componente trasmissiva do objeto

