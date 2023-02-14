class Uber(object):
    def __init__(self, nombre, placa, marca):
        self.nombre = nombre
        self.placa = placa
        self.marca = marca
    def printInfo(self):
        print(self.nombre,self.placa,self.marca)