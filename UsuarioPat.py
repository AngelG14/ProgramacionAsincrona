class UsuarioPat(object):

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedulo = cedula

    def getRut(self):
        return "Este es el rut de " + self.nombre
