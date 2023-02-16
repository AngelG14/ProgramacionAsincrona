from AplicacionUber import AplicacionUber
from UsuarioPat import UsuarioPat
from Dian import Dian
from ThreadRut import ThreadRut

if __name__ == '__main__':
    print("Ejemplo Promise")
    app = AplicacionUber("Pedro")
    app.runApp()
    print("Ejemplo thread")
    user = UsuarioPat("Oswaldo", 10721521)
    thread = ThreadRut(Dian(user.crearRut()))
    thread.start()
    print("Rut Enviado")

