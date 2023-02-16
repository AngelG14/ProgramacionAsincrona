import threading
import random
import time

class ThreadRut(threading.Thread):
    def __init__(self, siga):
        threading.Thread.__init__(self)
        self.dian = siga

    def run(self):
        time.sleep(random.randint(1, 3))
        self.dian.procesarRut()