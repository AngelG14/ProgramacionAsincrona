# import the threading module
import threading
import random
import time

class ThreadRut(threading.Thread):
    def __init__(self, dian):
        threading.Thread.__init__(self)
        self.dian = dian

        # helper function to execute the threads

    def run(self):
        time.sleep(random.randint(1, 3))
        self.dian.procesarRut()