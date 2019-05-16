class PointLigth():
    def __init__(self, position, color, intensity=1):
        self.type = 'Point'
        self.position = position
        self.color = color
        self.intensity = intensity

class DerectionLigth():
    def __init__(self, position, color, intensity=1):
        self.type = 'Directional'
        self.position = position
        self.color = color
        self.intensity = intensity