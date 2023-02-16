import asyncio
import random
from Uber import Uber

class AplicacionUber(object):

    def __init__(self, usuario):
        self.usuario = usuario

    def runApp(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.pedirUber())
        loop.close()

    async def pedirUber(self):
        print("Buscando Uber mas cercano.")
        try:
            uber = await self.buscarUber()
        except ValueError as exc:
            print('error:', exc.args[0])
        else:
            print(self.usuario, "Su uber es:")
            uber.printInfo()
            print("Llegara en", random.randint(1, 10), "minutos")

    async def buscarUber(self):
        await asyncio.sleep(random.randint(1, 3))
        return Uber("German", "REJ576", "Twingo")

    def getUsuario(self):
        return self.usuario
